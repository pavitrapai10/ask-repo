import os

CODE_EXTENSIONS = (".py", ".js", ".ts", "tsx", ".jsx", ".html", ".css", ".php", ".cpp", ".dart", ".go", ".java")

def scan_code_files(repo_path:str):
    code_files = []

    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(CODE_EXTENSIONS):
                file_path = os.path.join(root, file)
                code_files.append(file_path)

    return code_files