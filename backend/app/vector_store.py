from langchain_chroma import Chroma

def create_vector_store(chunks, embeddings):
    texts = [chunk["content"] for chunk in chunks ]
    metadatas = [{"path": chunk["path"]} for chunk in chunks]
    db = Chroma.from_texts(
        texts = texts, 
        embedding = embeddings, 
        metadatas = metadatas, 
        persist_directory = "vector_db"
    )
    return db