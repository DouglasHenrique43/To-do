import json
from utils.saveTheme import load_theme

class ThemeManager:
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.palette_name = load_theme()  # Carregar tema salvo
        self.themes = self.load_themes()
        self.active_button = None  # Armazena o botão ativo

    def load_themes(self):
        """
        Carrega as paletas de temas a partir de um arquivo JSON.
        """
        try:
            with open("src/theme/theme.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Erro: Arquivo 'theme.json' não encontrado.")
            return {}

    def set_theme(self, palette_name=None):
        """
        Aplica o tema à interface principal e aos botões da barra lateral.
        """
        palette_name = palette_name or self.palette_name  # Usa o tema salvo por padrão

        if palette_name not in self.themes:
            print(f"Paleta '{palette_name}' não encontrada. Usando '1' como padrão.")
            palette_name = "1"  # Paleta padrão em caso de erro

        theme = self.themes[palette_name]
        self.apply_styles(theme)

    def apply_styles(self, theme):
        """
        Aplica os estilos do tema à MainWindow.
        """
        mainColors = theme["mainColors"]
        primaryColors = theme["primaryColors"]
        secondaryColors = theme["secondaryColors"]
        thirdColors = theme["thirdColors"]
        smoothColors = theme["smoothColors"]
        strongColors = theme["strongColors"]

        # Atualiza o estilo principal
        self.MainWindow.setStyleSheet(f"""
            /* Estilos Gerais */
            QWidget {{
                border: none;
                color: {primaryColors['800']};
            }}
            QFrame {{
            }}
            QLabel {{
                border: none;
                border: transparent;
                background-color: none;
                border: 0px;
                background-color: transparent;
            }}
            QToolTip {{
                background-color: {mainColors['200']};; 
                color: white;               
                border: 1px solid {mainColors['500']};
                padding: 5px;               
                font-size: 12px;          
                height: 30px;               
            }}
            #content {{
                background-color: {mainColors['200']};
                font-family: 'Segoe UI';
            }}

            /* Scrollbars */
            {self.scrollbar_styles(mainColors, thirdColors)}

            /* Estilos do Topo */
            {self.top_styles(mainColors, thirdColors)}

            /* Estilos dos Botões Laterais */
            {self.sidebar_button_styles(mainColors, thirdColors)}

            /* Estilos do Extra */
            {self.extra_styles(mainColors, primaryColors)}

            /* Estilos de Configurações */
            {self.settings_styles(mainColors, primaryColors, thirdColors)}

            /* Estilos do Menu Superior */
            {self.top_menu_styles(mainColors, strongColors, primaryColors)}

            /* Estilos do Menu Inferior */
            {self.bottom_menu_styles(mainColors, strongColors, primaryColors, secondaryColors)}

            /* Estilos do Botão de Alternância */
            {self.toggle_button_styles(mainColors, strongColors)}

            /* Estilos do Conteúdo Extra */
            {self.extra_content_styles(mainColors, primaryColors, thirdColors, strongColors)}

            /* Estilos do Projeto */
            {self.project_styles(mainColors, primaryColors, secondaryColors, thirdColors, smoothColors, strongColors)}
        """)

    def scrollbar_styles(self, mainColors, thirdColors):
        return f"""
            /* Vertical Scrollbar */
            QScrollBar:vertical {{
                background-color: {thirdColors['400']};
                width: 1px; 
            }}
            QScrollBar::handle:vertical {{
                background-color: {mainColors['600']};
                min-height: 20px;
                border-radius: 1px;
            }}
            /* Horizontal Scrollbar */
            QScrollBar:horizontal {{
                background-color: {thirdColors['400']};
                height: 1px; 
            }}
            QScrollBar::handle:horizontal {{
                background-color: {mainColors['600']};
                min-width: 20px;
                border-radius: 1px;
            }}            
            QScrollBar::sub-line:vertical,
            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:horizontal,
            QScrollBar::add-line:horizontal {{
                background: none;
            }}
            QScrollBar::up-arrow:vertical,
            QScrollBar::down-arrow:vertical,
            QScrollBar::left-arrow:horizontal,
            QScrollBar::right-arrow:horizontal {{
                background: none; 
            }}
            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical,
            QScrollBar::add-page:horizontal,
            QScrollBar::sub-page:horizontal {{
                background: none; 
            }}
        """

    def top_styles(self, mainColors, thirdColors):
        return f"""
            /* Est ilos do Topo */
            #contentTopBg {{
                background-color: {mainColors['100']};
            }}
            #contentTopBg .QPushButton {{
                background-color: {thirdColors['400']};
                border: none;  
                border-radius: 5px; 
            }}
            #contentTopBg .QPushButton:hover {{
                background-color: {mainColors["700"]};
                border-style: solid; 
                border-radius: 4px;
            }}
            #contentTopBg .QPushButton:pressed {{
                background-color: {mainColors["900"]};
                border-style: solid; 
                border-radius: 4px; 
            }}
        """

    def sidebar_button_styles(self, mainColors, thirdColors):
        return f"""
            /* Estilos dos Botões Laterais */
            #rightButtons .QPushButton {{
                background-color: {thirdColors['400']};
                border: none;  
                border-radius: 5px; 
            }}
            #rightButtons .QPushButton:hover {{
                background-color: {mainColors["700"]};
                border-style: solid; 
                border-radius: 4px; 
            }}
            #rightButtons .QPushButton:pressed {{
                background-color: {mainColors["900"]};
                border-style: solid; 
                border-radius: 4px; 
            }}
        """

    def extra_styles(self, mainColors, primaryColors):
        return f"""
            /* Estilos do Extra */
            #extraRightBox {{
                background-color: {mainColors["300"]};
            }}
            #themeSettingsTopDetail {{
                background-color: {primaryColors["400"]};
            }}
            #bottomBar {{
                background-color: {mainColors["300"]};
            }}
            #bottomBar .QLabel {{
                font-size: 11px; 
                color: {mainColors["500"]};
                padding-left: 10px; 
                padding-right: 10px; 
                padding-bottom: 2px; 
            }}
        """

    def settings_styles(self, mainColors, primaryColors, thirdColors):
        return f"""
            /* Estilos de Configurações */
            #contentSettings .QPushButton {{	
                background-position: left center;
                background-repeat: no-repeat;
                border: none;
                border-left: 22px solid transparent;
                background-color: transparent;
                text-align: left;
                padding-left: 44px;
            }}
            #contentSettings .QPushButton:hover {{
                background-color: {mainColors["700"]};
            }}
            #contentSettings .QPushButton:pressed {{	
                background-color: {thirdColors['200']};
                color: {primaryColors['800']};
            }}
            #leftMenuBg {{	
                background-color: {mainColors['100']};
            }}
            #topLogo {{
                background-color: {mainColors['100']};
                background-image: url(:/images/images/PyDracula.png);
                background-position: centered;
                background-repeat: no-repeat;
            }}
            #titleLeftApp {{ 
                font: 63 12pt "Segoe UI Semibold"; 
            }}
            #titleLeftDescription {{ 
                font: 8pt "Segoe UI"; 
                color: {thirdColors['200']};
            }}
        """

    def top_menu_styles(self, mainColors, strongColors, primaryColors):
        return f"""
            /* Estilos do Menu Superior */
            #topMenu .QPushButton {{
                background-position: left center;
                background-repeat: no-repeat;
                border: none;
                border-left: 22px solid transparent;
                background-color: transparent;
                text-align: left;
                padding-left: 44px;
            }}
            #topMenu .QPushButton:hover {{
                background-color: {mainColors["700"]};
            }}
            #topMenu .QPushButton:pressed {{
                background-color: {strongColors["600"]};
                color: {primaryColors['900']};
            }}
        """

    def bottom_menu_styles(self, mainColors, strongColors, primaryColors, secondaryColors):
        return f"""
            /* Estilos do Menu Inferior */
            #bottomMenu .QPushButton {{	
                background-position: left center;
                background-repeat: no-repeat;
                border: none;
                border-left: 20px solid transparent;
                background-color: transparent;
                text-align: left;
                padding-left: 44px;
            }}
            #bottomMenu .QPushButton:hover {{
                background-color: {mainColors["700"]};
            }}
            #bottomMenu .QPushButton:pressed {{	
                background-color: {strongColors["600"]};
                color: {primaryColors['900']};
            }}
            #leftMenuFrame {{
                border-top: 3px solid {secondaryColors["100"]};
            }}
        """

    def toggle_button_styles(self, mainColors, strongColors):
        return f"""
            /* Estilos do Botão de Alternância */
            #toggleButton {{
                background-position: left center;
                background-repeat: no-repeat;
                border: none;
                border-left: 20px solid transparent;
                background-color: {mainColors["700"]};
                text-align: left;
                padding-left: 44px;
                color: {mainColors["500"]};
            }}
            #toggleButton:hover {{
                background-color: {mainColors["700"]};
            }}
            #toggleButton:pressed {{
                background-color: {strongColors["600"]};
            }}
        """

    def extra_content_styles(self, mainColors, primaryColors, thirdColors, strongColors):
        return f"""
            /* Estilos do Conteúdo Extra */
            #extraLeftBox {{
                background-color: {mainColors["300"]};
            }}
            #extraTopBg {{	
                background-color: {strongColors["600"]};
            }}
            #extraIcon {{
                background-position: center;
                background-repeat: no-repeat;
            }}
            #extraLabel {{ 
                color: {primaryColors['900']};
            }}
            #extraCloseColumnBtn {{ 
                background-color: {thirdColors['400']};
                border: none;  
                border-radius: 5px; 
            }}
            #extraCloseColumnBtn:hover {{ 
                background-color: {primaryColors['400']};
                border-style: solid; 
                border-radius: 4px; 
            }}
            #extraCloseColumnBtn:pressed {{ 
                background-color: {primaryColors['500']};
                border-style: solid; 
                border-radius: 4px; 
            }}
            #extraContent {{
                border-top: 3px solid {mainColors['200']};
            }}
            #extraTopMenu .QPushButton {{
                background-position: left center;
                background-repeat: no-repeat;
                border: none;
                border-left: 22px solid transparent;
                background-color: transparent;
                text-align: left;
                padding-left: 44px;
            }}
            #extraTopMenu .QPushButton:hover {{
                background-color: {mainColors['200']};
            }}
            #extraTopMenu .QPushButton:pressed {{	
                background-color: {strongColors["600"]};
                color: {primaryColors['900']};
            }}
        """

    def project_styles(self, mainColors, primaryColors, secondaryColors, thirdColors, smoothColors, strongColors):
        return f"""
            /* Estilos do Projeto */
            #projectLeftContent {{
                border-right: 3px solid qlineargradient(spread:pad, x1:0.5, y1:0.011, x2:0.5, y2:0.00568182, stop:0.97 {secondaryColors["100"]}, stop:1 {thirdColors["400"]});

            }}
            #searchProjectsButton {{
                /* Estilos do botão de busca de projetos */
            }}
            #searchBarFrame {{
                padding: 20px;
            }}
            #searchProjectsLineEdit {{
                font-family: Berlin Sans FB;
                background-color: transparent;
                font-size: 14px;
                color: {secondaryColors['400']};
            }}
            #searchProjectsLineEdit:focus {{
                border-bottom: 2px solid {mainColors['600']};
            }}
            #ProjectsTitle {{
                font-family: Berlin Sans FB;
                font-size: 35px;
                color: {primaryColors['800']};
            }}
            #addCategoryProjectButton {{
                width: 40px;
                height: 40px;
                border-radius: 5%;
                background-color: {mainColors['400']};
            }}
            #addCategoryProjectButton:hover {{
                background-color: {primaryColors['500']};
            }}
            #addCategoryProjectButton:pressed {{
                background-color: {mainColors['600']};
            }}
            #navProjectsFrame .QPushButton {{
                color: {secondaryColors['300']};
                border-bottom: 2px solid {secondaryColors['300']};
                font-weight: bold;
                font-size: 13px;
            }}
            #navProjectsFrame .QPushButton:hover {{
                color: {thirdColors['300']};
                border-bottom: 2px solid {thirdColors['300']};
                font-weight: bold;
                font-size: 13px;
            }}
            #navProjectsFrame .QPushButton:pressed {{
                color: {primaryColors['500']};
                border-bottom: 2px solid {primaryColors['500']};
                font-weight: bold;
                font-size: 13px;
            }}
            #projectScrollArea {{
                background-color: transparent;
            }}
            #projectRightContent {{
                background-color: {mainColors["700"]};
                border-top: 3px solid {mainColors["200"]};
            }}
            #titleCategoryPage {{
                font-family: Berlin Sans FB;
                color: {mainColors['600']};
                font-size: 40px;
            }}
            #newTaskButton {{
                border-radius: 5%;
                width: 120px;
                height: 40px;
                background-color: {mainColors['400']};
            }}
            #newTaskButton:hover {{
                background-color: {primaryColors['500']};
            }}
            #newTaskButton:pressed {{
                background-color: {mainColors['600']};
            }}
        """

    def change_theme(self, new_palette_name):
        """
        Altera o tema da aplicação e reaplica os estilos.
        """
        self.palette_name = new_palette_name
        self.set_theme(new_palette_name)