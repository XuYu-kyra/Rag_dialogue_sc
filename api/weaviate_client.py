import weaviate
from weaviate.auth import AuthApiKey
from sentence_transformers import SentenceTransformer
from .config import WEAVIATE_CONFIG

# 初始化embedding模型
embedding_model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
embedding_model.max_seq_length = 512
embedding_model.show_progress_bar = False

# 连接Weaviate
weaviate_client = weaviate.connect_to_custom(
    skip_init_checks=False,
    http_host=WEAVIATE_CONFIG['http_host'],
    http_port=WEAVIATE_CONFIG['http_port'],
    http_secure=False,
    grpc_host=WEAVIATE_CONFIG['http_host'],
    grpc_port=50051,
    grpc_secure=False,
    auth_credentials=AuthApiKey(WEAVIATE_CONFIG['api_key'])
)

def search_sunce(question, top_k=5):
    """
    在Weaviate数据库中执行语义搜索，返回最相关的历史文本
    
    :param question: 用户输入的问题
    :param top_k: 返回的文档数量
    :return: 包含text, source, speaker, relations, sources的列表
    """
    query_vector = embedding_model.encode(question).tolist()
    
    # 连接Weaviate集合
    collection = weaviate_client.collections.get("SunCeDocs")
    
    # 执行基于向量的最近邻搜索
    results = collection.query.near_vector(
        near_vector=query_vector,
        limit=top_k
    )
    
    # 解析查询结果
    retrieved_docs = []
    for res in results.objects:
        retrieved_docs.append({
            "text": res.properties.get("text", ""),
            "source": res.properties.get("source", "unknown"),
            "speaker": res.properties.get("speaker", "unknown"),
            "relations": res.properties.get("relations", ""),
            "sources": res.properties.get("sources", "")
        })
    
    return retrieved_docs 