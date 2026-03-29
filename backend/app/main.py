from fastapi import FastAPI, HTTPException
from app.repo_service import clone_repo
from app.file_service import scan_code_files, load_file_contents, chunk_documents
from app.embedding_service import get_embeddings
from app.vector_store import create_vector_store
app = FastAPI()


@app.get("/")
def home():
    return{"codebase ai assistant backend running"}


@app.post("/load-repo")
def load_repo(repo_url: str):

    if "github.com" not in repo_url:
        raise HTTPException(status_code=400, detail="Invalid github repo")

    try:
        repo_path = clone_repo(repo_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Clone failed: {str(e)}")

    try:
        files = scan_code_files(repo_path)
        documents = load_file_contents(files)
        chunks = chunk_documents(documents)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")

    try:
        embeddings = get_embeddings()
        vector_store = create_vector_store(chunks, embeddings)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Embedding failed: {str(e)}")

    return {
        "status": "success",
        "repo_path": repo_path,
        "total_files": len(files),
        "documents_loaded": len(documents),
        "total_chunks": len(chunks),
        "vector_db": "created successfully"
    }

    