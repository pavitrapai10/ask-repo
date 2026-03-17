from fastapi import FastAPI, HTTPException
from app.repo_service import clone_repo
from app.file_service import scan_code_files, load_file_contents, chunk_documents
app = FastAPI()


@app.get("/")
def home():
    return{"codebase ai assistant backend running"}


@app.post("/load-repo")
def load_repo(repo_url:str):

    if "github.com" not in repo_url:
        raise HTTPException(status_code=400, detail = "Invalid github repo")
    
    try:

        repo_path = clone_repo(repo_url)
        files = scan_code_files(repo_path)
        documents = load_file_contents(files)
        chunks = chunk_documents(documents)

        return{
            "status": "success",
            "message": "Repo cloned successfully", 
            "repo_path": repo_path,
            "total_files": len(files),
            "files": files[:20],
            "documents_loaded": len(documents),
            "total_chunks": len(chunks)

        }
    
    except Exception as e:
        raise HTTPException(status_code = 500, detail= f"Failed to clone repo {str(e)}")