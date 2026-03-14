import git
import os



def clone_repo(repo_url : str):
    repo_name = repo_url.split("/")[-1]
    repo_path = os.path.join("repos", repo_name)


    if not os.path.exists(repo_path):
        git.Repo.clone_from(repo_url, repo_path)


    return repo_path






