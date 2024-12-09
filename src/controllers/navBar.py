
from utils import *

# Lista de temas disponíveis
themes = ["1", "2"]

# Carregar o tema atual a partir da configuração
current_theme = load_theme()

# Encontrar o índice do tema carregado
current_theme_index = themes.index(current_theme)

def on_theme_button_click(main_window):
    """
    Lógica para alternar entre temas em sequência.
    :param main_window: Instância de MainWindow
    """
    global current_theme_index  # Variável para rastrear o índice atual

    # Incrementar o índice e garantir que ele volte ao início após o último tema
    current_theme_index = (current_theme_index + 1) % len(themes)

    # Obter o próximo tema
    new_theme = themes[current_theme_index]

    # Aplicar o tema com a instância existente do ThemeManager
    main_window.theme_manager.change_theme(new_theme)
    
    # Atualiza o tema atual na instância da janela
    main_window.currentTheme = new_theme

    # Salva o novo tema selecionado
    save_theme(new_theme)
