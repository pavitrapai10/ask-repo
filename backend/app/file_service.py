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


def load_file_contents(file_paths):

    documents = []

    for path in file_paths:

        try:

            with open(path, "r", encoding="utf-8") as f:

                content = f.read()

                documents.append({
                    "path": path,
                    "content": content
                })

        except Exception as e:

            print(f"Skipping file {path}: {e}")

    return documents


def chunk_documents(documents, chunk_size=500, overlap=100):

    chunks = []

    for doc in documents:

        content = doc["content"]
        path = doc["path"]

        start = 0

        while start < len(content):

            end = start + chunk_size

            chunk_text = content[start:end]

            chunks.append({
                "path": path,
                "content": chunk_text
            })

            start += chunk_size - overlap

    return chunks