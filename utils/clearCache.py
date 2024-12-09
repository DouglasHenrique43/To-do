import os
import shutil

# Definir o diretório base como o diretório atual
BASE_DIR = os.getcwd()  # Isso vai pegar o diretório onde o script está sendo executado

def remove_pycache(directory):
    """Remove todos os diretórios __pycache__ e arquivos tempCodeRunnerFile recursivamente."""
    for root, dirs, files in os.walk(directory, topdown=False):
        # Remover diretórios __pycache__
        for name in dirs:
            if name == "__pycache__":
                dir_path = os.path.join(root, name)
                shutil.rmtree(dir_path)
                print(f"Removido: {dir_path}")

        # Remover arquivos tempCodeRunnerFile
        for name in files:
            if name.startswith("tempCodeRunnerFile"):
                file_path = os.path.join(root, name)
                os.remove(file_path)
                print(f"Removido: {file_path}")

def clear():
    remove_pycache(BASE_DIR)
