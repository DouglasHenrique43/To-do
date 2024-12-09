# utils/saveTheme.py
import json
import os

# Função para carregar o tema salvo
def load_theme():
    try:
        with open(r"src\theme\theme_config.json", "r") as f:
            data = json.load(f)
            return data.get("currentTheme", "1")  # Retorna o tema salvo ou "GreyPalette" se não encontrado
    except FileNotFoundError:
        return "1"  # Tema padrão se não encontrar o arquivo

# Função para salvar o tema atual
def save_theme(theme):
    # Verifique se o diretório 'theme' existe, senão, crie
    if not os.path.exists('theme'):
        os.makedirs('theme')

    # Caminho do arquivo
    file_path = os.path.abspath(r"src\theme\theme_config.json")
    
    # Salvar o tema no arquivo JSON
    with open(file_path, "w") as f:
        json.dump({"currentTheme": theme}, f)
    
    print(f"Tema {theme} salvo em: {file_path}")  # Imprime o caminho absoluto onde o tema foi salvo
