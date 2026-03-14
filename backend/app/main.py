from fastapi import FastAPI, HTTPException
from app.repo_seervice import clone_repo
app = FastAPI()


@app.get("/")
def home():
    return{"codebase ai assistant backend running"}


@app.post("/load-repo")
def load_repo(repo_url:str):

    if "github.com" not in repo_url:
        raise HTTPException(status_code=400, detail = "Invalid github repo")
    
    try:

        path = clone_repo(repo_url)

        return{
            "message": "Repo cloned successfully", 
            "repo_path": path
        }
    
    except Exception as e:
        raise HTTPException(status_code = 500, detail= f"Failed to clone repo {str(e)}")