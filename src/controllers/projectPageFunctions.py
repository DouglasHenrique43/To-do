from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QPushButton, QWidget, 
    QLineEdit, QLabel, QFrame, QSizePolicy, QFileDialog, QListWidgetItem,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QTimer, QCoreApplication
from datetime import datetime

from components.loader import *
import os
import re
class ProjectFunctions:
    def __init__(self, MainWindow, QMainWindow, theme, loader=None):
        self.ui = MainWindow
        self.main_code = QMainWindow
        self.theme = theme
        self.loader = loader
        # Inicialização dos elementos
        self.init_ui_elements()
        self.ui.projectsPagesStacked.setCurrentWidget(self.ui.Projects_HomePage)


        # Criar um QTimer para atualizar a data/hora
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_registerProject_date)

        # Inicializar outras configurações
        self.applyPageStyles()
        self.setup_layout()
        self.setup_connections()
        self.category_colors = {}
        self.strong_color_index = 0
        self.setTitleName(self.currentPage())
        self.updateCategoryCount()
        self.check_and_hide_task_frame()
        # Atualizar o título inicial
        self.updateTitle()
        self.personalizedItemListWidget()
        # Atributos para armazenar informações do projeto
        self.project_name = ""
        self.creation_date = ""
        self.description = ""
        self.deadline = ""
        self.priority = ""
        self.tags = []
        self.files = []

    def init_ui_elements(self):
        """ Initializes the UI elements """
        self.searchProjectsButton = self.ui.searchProjectsButton
        self.searchProjectsLineEdit = self.ui.searchProjectsLineEdit
        self.addCategoryProjectButton = self.ui.addCategoryProjectButton
        self.allProjectsButton = self.ui.allProjectsButton
        self.openProjectsButton = self.ui.openProjectsButton
        self.closedProjectsButton = self.ui.closedProjectsButton
        self.projectScrollContent = self.ui.projectScrollContent
        self.titleCategorysPage = self.ui.titleCategoryPage
        self.tasksNumbers = self.ui.tasksNumbers
        self.categoryTitles = self.ui.ProjectsTitle 
        self.filesBox = self.ui.attachmentsList
        print(f"creationDateEdit initialized: {self.ui.creationDateEdit}")  # Debugging
        
    def setup_layout(self):
        """ Configures the layout for the project scroll area """
        self.scrollLayout = QVBoxLayout(self.projectScrollContent)
        self.scrollLayout.setAlignment(Qt.AlignTop)
        self.projectScrollContent.setLayout(self.scrollLayout)




    def setup_connections(self):
        """ Sets up signal and slot connections """
        self.allProjectsButton.clicked.connect(lambda: self.setActiveButton(self.allProjectsButton))
        self.openProjectsButton.clicked.connect(lambda: self.setActiveButton(self.openProjectsButton))
        self.closedProjectsButton.clicked.connect(lambda: self.setActiveButton(self.closedProjectsButton))
        self.addCategoryProjectButton.clicked.connect(lambda: self.addCategoryInput())

        # Conectar a mudança de página ao método de atualização do título
        self.ui.projectsPagesStacked.currentChanged.connect(self.updateTitle)
        # Conectar a mudança de página ao método que verifica e esconde o task frame
        self.ui.projectsPagesStacked.currentChanged.connect(self.check_and_hide_task_frame)
        # Conectar a mudança de página ao método que reabilita o botão "New Project"
        self.ui.projectsPagesStacked.currentChanged.connect(self.reenableNewProjectButton)

        self.setActiveButton(self.allProjectsButton)



    def setActiveButton(self, active_button):
        """ Define o botão ativo e aplica o estilo """
        self.resetButtonStyles()  # Reseta o estilo de todos os botões
        self.applyButtonStyle(active_button)  # Aplica o estilo ao botão ativo
        self.active_button = active_button
        active_button.setObjectName("projectsNavButtonActive")
        print(f"Botão ativo: {self.active_button.text()}")

    def resetButtonStyles(self):
        """ Reseta o estilo de todos os botões de navegação """
        navButtons = self.ui.navProjectsFrame.findChildren(QPushButton)
        for btn in navButtons:
            btn.setStyleSheet(f"color: {self.theme['secondaryColors']['300']};")

    def applyButtonStyle(self, button):
        """ Aplica o estilo ao botão ativo """
        button.setStyleSheet(f"color: {self.theme['mainColors']['600']}; border-bottom: 2px solid {self.theme['mainColors']['600']}")

    def addCategoryInput(self):
        """ Exibe o campo de entrada para o título da categoria diretamente no layout """
        self.addCategoryProjectButton.setDisabled(True)

        # Criação do campo de texto para digitar o nome da categoria
        categoryInput = QLineEdit(self.projectScrollContent)
        categoryInput.setPlaceholderText("Category name")
        categoryInput.setStyleSheet(f"font-weight: bold; font-size: 14px; padding: 5px; border-bottom: 2px solid {self.theme['mainColors']['400']}; background-color: transparent;")
        
        # Adiciona o campo de entrada ao layout
        self.scrollLayout.addWidget(categoryInput)

        # Focar no campo de entrada
        categoryInput.setFocus()

        # Conectar o evento de pressionamento da tecla Enter para adicionar a categoria
        categoryInput.returnPressed.connect(lambda: self.addCategory(categoryInput.text(), categoryInput))

    def addCategory(self, category_title, categoryInput):
        """ Adiciona a categoria ao layout sem projetos inicialmente """
        if not category_title.strip():
            print("Erro: O título da categoria não pode estar vazio.")
            # Remover a categoria de input se estiver vazia
            self.scrollLayout.removeWidget(categoryInput)
            categoryInput.deleteLater()

            # Reabilitar o botão de adicionar categoria
            self.addCategoryProjectButton.setDisabled(False)

            # Retornar o foco ao botão de adicionar categoria
            self.addCategoryProjectButton.setFocus()

            return

        # Verifica se já existe uma categoria com o mesmo título
        existing_category = self.scrollLayout.parent().findChild(QPushButton, f"categoryButton_{category_title.replace(' ', '_')}")
        if existing_category:
            self.main_code.show_alert(self.theme['smoothColors']['200'], self.theme['strongColors']['800'], r'src\assets\icons\PhXCircleDuotone.svg', f'Error: {category_title} already registered')        
            categoryInput.clear()  # Limpa o campo de entrada para o usuário tentar outro nome
            return

        # Armazenar a cor da categoria no momento da criação
        strong_color_key, strong_color_value = self.updateStrongColors()
        self.category_colors[category_title] = strong_color_key  # Armazena a chave da cor associada ao título

        projects = []  # Lista vazia de projetos (sem projetos inicialmente)
        self.accordion(category_title, projects, strong_color_key)  # Passar a cor da categoria para o accordion

        # Remover o campo de texto após a categoria ser adicionada
        self.scrollLayout.removeWidget(categoryInput)
        categoryInput.deleteLater()
        self.main_code.show_alert(self.theme['smoothColors']['400'], self.theme['strongColors']['500'], r'src\assets\icons\SolarCheckCircleBoldDuotone.svg', f'Success: Category {category_title} registered')        
        self.addCategoryProjectButton.setDisabled(False)
        self.ui.centralwidget.setUpdatesEnabled(False)
        self.ui.centralwidget.setUpdatesEnabled(True)

        # Atualiza a contagem de categorias
        self.updateCategoryCount()


    def accordion(self, title, projects, strong_color_key):
        """ Adiciona um accordion de categoria ao layout sem projetos """
        # Título original
        button_title = title

        # Verificar se o título excede 15 caracteres
        if len(button_title) > 22:
            button_title = button_title[:15] + "..."

        # Criar o botão com o título truncado
        categoryButton = QPushButton(button_title)
        categoryButton.setCheckable(True)
        categoryButton.setChecked(True)
        categoryButton.setStyleSheet(f"""
            font-family: Berlin Sans FB;
            font-size: 18px;
            text-align: left;
            padding: 10px;
            color: {self.theme['secondaryColors']['300']};
        """)
        categoryButton.setCursor(Qt.PointingHandCursor)
        categoryButton.setObjectName(f"categoryButton_{title.replace(' ', '_')}")

        icon = QLabel()
        icon.setPixmap(QPixmap(":/icons/icons/IconParkOutlineUp.svg"))
        icon.setAlignment(Qt.AlignRight)
        categoryButton.setIcon(QPixmap(":/icons/icons/IconParkOutlineUp.svg"))
        categoryButton.setIconSize(icon.sizeHint())

        categoryButton.setLayoutDirection(Qt.RightToLeft)

        contentWidget = QWidget()
        contentLayout = QVBoxLayout(contentWidget)
        contentLayout.setContentsMargins(0, 0, 0, 0)
        contentWidget.setObjectName(f"contentWidget_{title.replace(' ', '_')}")
        contentWidget.setVisible(True)

        if not projects:
            noProjectLabelText = f"Wait'ing something..."

            # Verificar se o título excede 15 caracteres
            if len(noProjectLabelText) > 30:
                noProjectLabelText = noProjectLabelText[:30] + "..."

            # Criar o QLabel com o texto ajustado
            noProjectLabel = QLabel(noProjectLabelText)
            noProjectLabel.setObjectName(f"noProjectLabel_{title.replace(' ', '_')}")
            noProjectLabel.setStyleSheet(f"font-size: 14px; color: {self.theme['mainColors']['500']}; padding: 10px; background-color: transparent; border: transparent; border: none; background-color: none")
            contentLayout.addWidget(noProjectLabel)

        addProjectButton = QPushButton(" New Project")
        addProjectButton.setIcon(QPixmap(":/icons/icons/TablerPlus.svg"))
        addProjectButton.setIconSize(icon.sizeHint())
        addProjectButton.setStyleSheet(f"""
            font-size: 14px; 
            color: {self.theme['primaryColors']['800']};
            background-color: qlineargradient(spread:repeat, x1:0.669, y1:0.801, x2:0.742, y2:0.823364, stop:0.478022 {self.theme['primaryColors']['700']}, stop:0.483516 rgba(255, 255, 255, 0));
            
            border-radius: 6px;
            padding: 5px;
            margin-top: 10px;
        """)
        addProjectButton.setCursor(Qt.PointingHandCursor)
        addProjectButton.clicked.connect(lambda: self.addNewProject(title))

        addProjectButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        addProjectButton.setMinimumHeight(100)

        contentLayout.addWidget(addProjectButton)

        categoryButton.toggled.connect(lambda checked: self.toggleIcon(checked, categoryButton, contentWidget))

        self.scrollLayout.addWidget(categoryButton)
        self.scrollLayout.addWidget(contentWidget)


    def toggleIcon(self, checked, categoryButton, contentWidget):
        """ Troca o ícone baseado no estado expandido ou contraído e mostra/oculta o conteúdo """
        if checked:
            categoryButton.setIcon(QPixmap(":/icons/icons/IconParkOutlineUp.svg"))
            contentWidget.setVisible(True)
        else:
            categoryButton.setIcon(QPixmap(":/icons/icons/MingcuteDownFill.svg"))
            contentWidget.setVisible(False)

    def addNewProject(self, category_title):
        """ Solicita o nome do projeto e adiciona-o à categoria """
        print(f"Adicionando novo projeto à categoria: {category_title}")

        # Desabilitar o botão "New Project" enquanto o projeto está sendo adicionado
        categoryContentWidget = self.scrollLayout.parent().findChild(QWidget, f"contentWidget_{category_title.replace(' ', '_')}")
        if categoryContentWidget:
            addProjectButton = categoryContentWidget.findChild(QPushButton)
            if addProjectButton:
                addProjectButton.setDisabled(True)

        # Passando o loader para a página de registro de projetos
        loader_instance = CircularLoader(ui=self.ui)  # Cria uma nova instância do loader
        loader_instance.start()  # Isso irá bloquear até o progresso atingir 100%

        # Aqui você redireciona para a página de registro de projetos
        self.ui.projectsPagesStacked.setCurrentWidget(self.ui.Register_ProjectPage)

        # Se você precisar passar informações para a página de registro de projetos, você pode fazer isso aqui
        self.current_category_title = category_title  # Armazena a categoria atual

        loader_instance.hide()  # Oculta o loader


    def registerProject_info(self):
        # Aqui você pode preencher os campos com os valores armazenados
        self.ui.projectNameEdit.setText(self.project_name)
        self.ui.creationDateEdit.setText(self.creation_date)
        self.ui.descriptionTextEdit.setPlainText(self.description)
        self.ui.deadlineEdit.setText(self.deadline)
        self.ui.priorityComboBox.setCurrentText(self.priority)
        self.ui.tagsEdit.setText(", ".join(self.tags))  # Supondo que você armazene tags como uma lista
        # Para arquivos, você pode adicionar lógica para preencher a lista de arquivos

    def reenableNewProjectButton(self):
        """ Reabilita o botão 'New Project' quando sai da página de registro """
        if self.ui.projectsPagesStacked.currentWidget() != self.ui.Register_ProjectPage:
            categoryContentWidget = self.scrollLayout.parent().findChild(QWidget, f"contentWidget_{self.current_category_title.replace(' ', '_')}")
            if categoryContentWidget:
                addProjectButton = categoryContentWidget.findChild(QPushButton)
                if addProjectButton:
                    addProjectButton.setDisabled(False)
                    print("Botão 'New Project' reabilitado.")

    def addProjectToCategory(self, project_title, projectInput, category_title, strong_color_key, addProjectButton):
        """ Adiciona o projeto ao layout da categoria """
        if not project_title.strip():
            print("Erro: O título da categoria não pode estar vazio.")
            # Remover a categoria de input se estiver vazia
            self.scrollLayout.removeWidget(projectInput)
            projectInput.deleteLater()

            
            addProjectButton.setDisabled(False)

            return

        # Caso o título do projeto não seja vazio, continua com o processo de adicionar o projeto
        self.scrollLayout.removeWidget(projectInput)
        projectInput.deleteLater()
        addProjectButton.setDisabled(False)


        # Adicionar as Labels no lado esquerdo
        projectTitle = QLabel(project_title)
        projectTitle.setObjectName(f"projectTitle_{category_title.replace(' ', '_')}")
        projectTitle.setStyleSheet(f"font-size: 16px; color: {self.theme['mainColors']['500']};")

        numberOfTasks = QLabel("Tasks: 0")
        numberOfTasks.setObjectName(f"numberOfTasks_{category_title.replace(' ', '_')}")

        # Adiciona o conteúdo do lado direito (como o "project_label")
        project_label = QLabel(f"Project in {category_title}")
        project_label.setObjectName(f"projectLabel_{category_title.replace(' ', '_')}")

        # Criar o cartão do projeto
        project_card = QWidget()
        project_card.setFixedHeight(100)
        project_card.setMaximumHeight(100)
        project_card.setMaximumWidth(360)
        project_cardLayout = QHBoxLayout(project_card)
        project_cardLayout.setContentsMargins(0, 0, 0, 0)
        project_cardLayout.setSpacing(0)  # Remove o espaçamento entre os widgets no layout

        left = QFrame()
        leftLayout = QVBoxLayout(left)
        project_cardLayout.setContentsMargins(0, 0, 0, 0)
        project_cardLayout.addWidget(left)
        left.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        right = QFrame()
        rightLayout = QHBoxLayout(right)
        project_cardLayout.setContentsMargins(0, 0, 0, 0)
        project_cardLayout.addWidget(right)



        leftLayout.addWidget(projectTitle)
        leftLayout.addWidget(numberOfTasks)

        rightLayout.addWidget(project_label)
        rightLayout.addWidget(project_label)



        # Agora, o cartão deve exibir os widgets no layout correto: 


        # Encontrar o contentWidget da categoria onde o projeto será adicionado
        categoryContentWidget = self.scrollLayout.parent().findChild(QWidget, f"contentWidget_{category_title.replace(' ', '_')}")

        if categoryContentWidget:
            # Obter o layout do contentWidget
            contentLayout = categoryContentWidget.layout()

            # Remover "Wait'ing something..." se for o único item no layout
            noProjectLabel = categoryContentWidget.findChild(QLabel, f"noProjectLabel_{category_title.replace(' ', '_')}")
            if noProjectLabel:
                contentLayout.removeWidget(noProjectLabel)
                noProjectLabel.deleteLater()

            # Localizar o botão "New Project"
            addProjectButton = categoryContentWidget.findChild(QPushButton)

            # Remover temporariamente o botão "New Project" do layout
            if addProjectButton:
                contentLayout.removeWidget(addProjectButton)

            # Adicionar o cartão do projeto ao layout do contentWidget
            contentLayout.addWidget(project_card)

            # Recolocar o botão "New Project" no final do layout
            if addProjectButton:
                contentLayout.addWidget(addProjectButton)

            # Aplicar o tema nos botões dentro do contentWidget
            self.applyThemeToButtonsInContentWidget(category_title, strong_color_key)
            self.main_code.show_alert(self.theme['smoothColors']['300'], self.theme['strongColors']['400'], r'src\assets\icons\SolarCheckCircleBoldDuotone.svg', f'Novo projeto adicionado.')

            print(f"Projeto '{project_title}' adicionado à categoria: {category_title}")
        else:
            print(f"Erro: Não foi possível encontrar a categoria '{category_title}'")

    def updateStrongColors(self):
        """ Atualiza o índice da cor em 'strongColors' de forma cíclica e associa à nova categoria """
        color_keys = list(self.theme['strongColors'].keys())  # Obtém todas as chaves (ex: '100', '200', '300', etc.)
        
        # Incrementa o índice de forma cíclica
        self.strong_color_index = (self.strong_color_index + 1) % len(color_keys)
        
        # Obtém a chave correspondente à cor
        strong_color_key = color_keys[self.strong_color_index]
        
        # Agora a cor será associada à nova categoria
        return strong_color_key, self.theme['strongColors'][strong_color_key]
            
    def applyThemeToButtonsInContentWidget(self, category_title, strong_color_key):
        """ Aplica o tema a todos os botões dentro do widget da categoria """
        categoryContentWidget = self.scrollLayout.parent().findChild(QWidget, f"contentWidget_{category_title.replace(' ', '_')}")
        
        if categoryContentWidget:
            frames = categoryContentWidget.findChildren(QFrame)

            # Aplica o estilo aos widgets da categoria com a cor específica
            for frame in frames:
                frame.setStyleSheet(f"""
                    QFrame {{
                        font-family: Berlin Sans FB;
                        font-size: 18px;
                        background-color: {self.theme['mainColors']['900']};
                        border-bottom-right-radius: 3px;
                        border-top-right-radius: 3px;
                    }}
                    QLabel{{
                        color: {self.theme['mainColors']['400']};
                    }}
                """)
        else:
            print(f"Erro: Não foi possível encontrar o widget da categoria '{category_title}'")

    def applyPageStyles(self):
        """ Applies the stylesheet to the current page or relevant widgets """
        style = self.pagesStyles()
        self.ui.centralwidget.setStyleSheet(style)  # Central widget ou qualquer outro alvo principal


    def currentPage(self):
        """ Obtém o nome da página atual """
        current_page_index = self.ui.projectsPagesStacked.currentIndex()
        current_widget = self.ui.projectsPagesStacked.widget(current_page_index)

        if current_widget:
            # Obtém o nome do objeto
            page_name = current_widget.objectName()

            # Depuração para verificar o nome do objeto
            print(f"Raw objectName: {repr(page_name)}")

            # Substitui os underscores por espaços
            formatted_name = page_name.replace("_", " ")

            # Converte de camelCase para formato com espaços
            formatted_name = re.sub(r'([a-z])([A-Z])', r'\1 \2', formatted_name)

            # Remove "Page" do final, se existir
            if formatted_name.endswith("Page"):
                formatted_name = formatted_name[:-4].strip()
        else:
            formatted_name = "Unknown Page"

        print(f"Formatted name: {formatted_name}")  # Para depuração
        return formatted_name

    def check_and_hide_task_frame(self):
        """ Atualiza e limpa a data conforme a página ativa """
        current_page_name = self.currentPage()  # Obtém o nome da página atual
        task_frame = self.ui.taskFrame  # Inicializa `task_frame`
        creation_date_edit = self.ui.creationDateEdit  # Campo de data (substitua pelo correto)

        if current_page_name == "Register Project":
            # Exibe o task frame e seus filhos
            task_frame.setVisible(False)
            for child in task_frame.findChildren(QWidget):
                child.setVisible(False)

            # Define a data/hora no campo
            if creation_date_edit:
                current_datetime = datetime.now().strftime("%d/%m/%Y")
                creation_date_edit.setText(current_datetime)
                print(f"Data definida no campo: {current_datetime}")
            else:
                print("Campo de edição de data não encontrado!")
        else:
            # Oculta o task frame e seus filhos
            task_frame.setVisible(True)
            for child in task_frame.findChildren(QWidget):  # Encontrar todos os filhos do taskFrame
                child.setVisible(True)

            # Limpa o texto do campo de data
            if creation_date_edit:
                creation_date_edit.clear()
                print("Campo de data limpo.")
            else:
                print("Campo de edição de data não encontrado!")

    def updateTitle(self):
        """ Atualiza o título da página atual """
        current_title = self.currentPage()
        self.setTitleName(current_title)


    def update_registerProject_date(self):
        """ Atualiza a data/hora no campo da página Register_ProjectPage """
        current_datetime = datetime.now().strftime("%d/%m/%Y")  # Formato atualizado
        try:
            if self.ui.creationDateEdit:
                self.ui.creationDateEdit.setText(current_datetime)
                print(f"Data e hora atualizadas para: {current_datetime}")
            else:
                print("Campo 'creationDateEdit' não encontrado.")
        except AttributeError as e:
            print(f"Erro ao atualizar a data/hora: {e}")

    def pagesStyles(self):
        """ Applies the styles to different pages """
        return f"""
            #projectNameLabel, #creationDateLabel, #descriptionLabel, #deadlineLabel,
            #priorityLabel, #initialStatsLabel, #tagsLabel, #attachmentsLabel {{
                font-family: Berlin Sans FB;
                font-size: 20px;
                color: {self.theme['primaryColors']['400']};
            }}
            #attachmentsMessageLabel {{
                font-family: Berlin Sans FB;
                font-size: 15px;
                color: {self.theme['secondaryColors']['400']};
            }}
            #projectNameEdit, #deadlineEdit, #tagsEdit, #descriptionTextEdit {{
                font-family: Berlin Sans FB;
                font-size: 17px;
                height: 30px;
                padding: 4px;
                border-bottom: 2px solid {self.theme['primaryColors']['600']};
                background-color: transparent;
                color: {self.theme['secondaryColors']['400']};
            }}
            
            #projectNameEdit:focus, #deadlineEdit:focus, #tagsEdit:focus, #descriptionTextEdit:focus {{
                border-bottom: 2px solid {self.theme['mainColors']['600']};
                color: {self.theme['primaryColors']['800']};
            }}
            #creationDateEdit {{
                width: 50px;
                height: 30px;
                border-radius: 5px;
                background-color: {self.theme['strongColors']['1400']};
                color: {self.theme['strongColors']['1500']};
                font-family: Berlin Sans FB;
                font-size: 17px;
                padding: 3px;
                text-align: center;
            }}

            QComboBox {{
                border: 2px solid {self.theme['primaryColors']['900']};
                background-color: {self.theme['primaryColors']['300']};
                border-radius: 5px;
                padding: 5px;
                height: 25px;
                font-family: 'Berlin Sans FB';
                font-size: 16px;
            }}
            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 25px;
                border: none;
            }}
            QComboBox::down-arrow {{
                image: url('src/assets/icons/cil-arrow-bottom.png'); /* Substitua pelo caminho do seu SVG */
                width: 15px; /* Ajuste o tamanho do ícone */
                height: 15px;
            }}   
            /* Estilizando os itens dentro da lista de opções */
            QComboBox QAbstractItemView {{
                background-color: {self.theme['primaryColors']['600']};
                padding: 10px;
                font-family: Berlin Sans FB;
                color: {self.theme['primaryColors']['800']};
                outline: none; /* Remove qualquer borda pontilhada associada ao foco */
            }}
            QComboBox QAbstractItemView::item {{
                padding-left: 10px;  /* Espaçamento à esquerda */
                padding-right: 10px; /* Espaçamento à direita */
                min-height: 30px;    /* Altura mínima de cada item */
            }}

     
            #addProjectFilesButton {{
                width: 150px;
                height: 37px;
                border-radius: 15px;
                background-color: {self.theme['primaryColors']['500']};
            }}
            #filterFilesFrame {{
                height: 25px;
                background-color: {self.theme['secondaryColors']['300']};
                padding-left: 8px;
                padding-right: 8px;
                padding-top: 2px;
                padding-bottom: 2px;
                border-radius: 20px;

            }}
            #filterFilesEdit {{
                width: 150px;
                font-family: Berlin Sans FB;
                font-size: 17px;
                height: 30px;
                padding: 4px;
                background-color: transparent;
                border: none;
                color: {self.theme['primaryColors']['800']};
            }}
            #filterButtonIcon {{
                background-color: transparent;
                border: none;
            }}
            #clearFilterProjectButton {{
                width: 30px;
                height: 30px;
                border-radius: 15%;
                background-color: {self.theme['secondaryColors']['400']};
            }}
            #clearFilterProjectButton:hover {{
                background-color: {self.theme['secondaryColors']['700']};
            }}
            #clearFilterProjectButton:pressed {{
                background-color: {self.theme['secondaryColors']['200']};
            }}

            #cancelRegisterProjectButton {{
                height: 30px; 
                width: 150px;
                border-radius: 15px;
                border: 2px solid {self.theme['primaryColors']['400']};
                color: {self.theme['primaryColors']['400']};
                font-weight: bold;
                font-size: 18px;
                font-family: Calibri;
            }}
            #confirmRegisterProjectButton {{
                height: 30px; 
                width: 150px;
                border-radius: 15px;
                background-color: {self.theme['primaryColors']['400']};
                color: {self.theme['mainColors']["700"]};
                font-weight: bold;
                font-size: 18px;
                font-family: Calibri;
            }}
            #attachmentsList {{
                background-color: transparent;
            }}
            #attachmentsFilesFrame {{
                background-color: {self.theme['mainColors']['300']};
                border-radius: 10px;
                padding: 10px;
            }}
            #addFilesProjectProgress {{
                background-color: transparent;
            }}
            #addFilesProjectProgress::chunk {{
                background-color: #4caf50;  # Cor do progresso (verde)
            }}
        """


    def updateCategoryCount(self):
        """ Atualiza o título com o número total de categorias na área de rolagem """
        # Filtra os widgets no layout para contar os botões de categoria
        category_count = sum(
            1 for widget in self.scrollLayout.parentWidget().findChildren(QPushButton)
            if widget.objectName().startswith("categoryButton_")
        )
        
        # Define o título base (sem contador)
        base_title = "Categories"  # Altere conforme necessário
        
        # Define o texto final com o contador
        new_text = f"{base_title} <span style='font-size: 16px; font-family: calibri; font-weight: bold; color: {self.theme['mainColors']['400']};'>({category_count})</span>"
        
        # Atualiza o QLabel com o novo texto
        self.categoryTitles.setText(new_text)

    def setTitleName(self, title):
        """ Define o nome do título na barra superior """
        if not self.titleCategorysPage:
            print("Erro: titleCategorysPage não inicializado corretamente.")
            return
        
        print(f"Atualizando título para: {title}")
        self.titleCategorysPage.setText(title)
        self.titleCategorysPage.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def personalizedItemListWidget(self):
        """
        Inicializa as conexões e configura os widgets existentes.
        """
        self.ui.addProjectFilesButton.clicked.connect(lambda: self.add_file())
        self.ui.filterFilesEdit.textChanged.connect(self.filter_files)  # Conectar ao filtro


    def create_file_item_widget(self, index, file_name, file_format, file_size, file_path):
        """
        Cria um widget personalizado para o item da lista com elementos fixos e alinhados.
        """
        widget = QWidget()
        layout = QHBoxLayout(widget)

        # Elementos do widget
        index_label = QLabel(f"{index}")
        index_label.setFixedWidth(45)
        index_label.setFixedHeight(30)
        index_label.setAlignment(Qt.AlignCenter)
        index_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Tamanho fixo horizontal e vertical

        # Estilos CSS corrigidos
        index_label.setStyleSheet(f"""
            height: 25px;
            background-color: {self.theme['strongColors']['1400']};
            color: {self.theme['primaryColors']['800']};
            font-family: Berlin Sans FB;
            font-size: 17px;
            padding: 3px;
            text-align: center;
            border-radius: 8px;
        """)

        file_name_label = QLabel(file_name)
        file_name_label.setStyleSheet(f"""
            padding-left: 10px;
        """)
        file_name_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)  # Alinha à esquerda e verticalmente ao centro
        file_name_label.setToolTip("File name")  # Tooltip
        file_name_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # Expande horizontalmente

        file_format_label = QLabel(file_format)
        file_format_label.setFixedWidth(170)
        file_format_label.setAlignment(Qt.AlignCenter)
        file_format_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Tamanho fixo
        file_format_label.setToolTip("File format")  # Tooltip

        file_size_label = QLabel(f"{file_size} KB")
        file_size_label.setFixedWidth(170)
        file_size_label.setAlignment(Qt.AlignCenter)
        file_size_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Tamanho fixo
        file_size_label.setToolTip("File size in kilobytes")  # Tooltip

        # Adicionar uma nova label para o caminho do arquivo
        file_path_label = QLabel(file_path)  # A nova label para o caminho do arquivo
        file_path_label.setStyleSheet(f"""
            font-size: 12px;
            color: gray;
            padding-left: 10px;
        """)
        file_path_label.setToolTip("File path")  # Tooltip
        file_path_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Expande horizontalmente

        edit_button = QPushButton("Edit")
        edit_button.setFixedWidth(90)
        edit_button.setFixedHeight(30)
        edit_button.setObjectName("edit_button")  # Nome do objeto
        edit_button.setIcon(QIcon("src/assets/icons/plus.svg"))  # Caminho para o ícone de edição
        edit_button.setToolTip("Edit file details")  # Tooltip
        edit_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Tamanho fixo
        edit_button.setStyleSheet(f"""
            #{edit_button.objectName()} {{
                border-radius: 5px;
                background-color: {self.theme['secondaryColors']['400']};
                border: none;
            }}

            #{edit_button.objectName()}:hover {{
                background-color: {self.theme['secondaryColors']['500']};
            }}
        """)

        delete_button = QPushButton("")
        delete_button.setFixedWidth(30)
        delete_button.setFixedHeight(30)
        delete_button.setIcon(QIcon("src/assets/icons/x.svg"))  # Caminho para o ícone de exclusão
        delete_button.setObjectName("delete_button")  # Nome do objeto
        delete_button.setToolTip("Delete file")  # Tooltip
        delete_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Tamanho fixo
        delete_button.setStyleSheet(f"""
            #{delete_button.objectName()} {{
                border-radius: 15%;
                background-color: {self.theme['secondaryColors']['400']};
                border: none;
            }}

            #{delete_button.objectName()}:hover {{
                background-color: {self.theme['secondaryColors']['500']};
            }}
        """)

        # Armazenar referências no widget
        widget.index_label = index_label
        widget.file_name_label = file_name_label
        widget.file_format_label = file_format_label
        widget.file_size_label = file_size_label
        widget.file_path_label = file_path_label  # Adicionar o caminho do arquivo ao widget

        # Adicionar elementos ao layout
        layout.addWidget(index_label)
        layout.addWidget(file_name_label)
        layout.addWidget(file_path_label)  # Adicionar a label do caminho
        layout.addWidget(file_format_label)
        layout.addWidget(file_size_label)
        layout.addWidget(edit_button)
        layout.addWidget(delete_button)

        # Ajustes do layout
        layout.setContentsMargins(9, 9, 9, 9)
        layout.setSpacing(18)

        return widget, edit_button, delete_button

    def add_file(self):
        """
        Abre o diálogo de seleção de arquivos e adiciona arquivos ao QListWidget, um por vez, sem travar a tela.
        """
        # Desativar o filtro enquanto os arquivos são carregados
        self.ui.filterFilesEdit.setDisabled(True)

        # Mostrar a caixa de diálogo para selecionar arquivos
        file_paths, _ = QFileDialog.getOpenFileNames(None, "Select Files", "", "All Files (*)")
        
        if file_paths:
            total_files = len(file_paths)  # Quantidade total de arquivos
            for idx, file_path in enumerate(file_paths):
                # Verificar se o arquivo já está na lista
                if self.is_file_in_list(file_path):
                    continue  # Pula a iteração se o arquivo já estiver presente

                file_name = os.path.basename(file_path)
                file_name = os.path.splitext(file_name)[0]  # Pega o nome do arquivo sem a extensão
                file_format_base = os.path.splitext(file_path)[1].lstrip(".") or 'None'  # Pega a extensão sem o ponto
                file_format = f'.{file_format_base.upper()}'
                # Verifica se o nome do arquivo tem mais de 15 caracteres
                if len(file_name) > 15:
                    file_name = file_name[:15] + "..."  # Trunca o nome e adiciona "..."
                file_size = round(os.path.getsize(file_path) / 1024, 2)  # Tamanho em KB
                index = self.ui.attachmentsList.count() + 1

                # Criar o widget personalizado para o arquivo e adicionar o file_path
                item_widget, edit_button, delete_button = self.create_file_item_widget(index, file_name, file_format, file_size, file_path)

                # Armazenar o caminho do arquivo no widget
                item_widget.file_path = file_path

                # Criar o item da lista e associar o widget
                list_item = QListWidgetItem(self.ui.attachmentsList)
                list_item.setSizeHint(item_widget.sizeHint())
                self.ui.attachmentsList.addItem(list_item)
                self.ui.attachmentsList.setItemWidget(list_item, item_widget)

                # Conectar os botões às funções
                self.connect_file_item_buttons(self.ui.attachmentsList, edit_button, delete_button, index)

                # Atualizar a barra de progresso: calcular o progresso
                progress_value = int(((idx + 1) / total_files) * 100)
                self.ui.addFilesProjectProgress.setValue(progress_value)

                # Permitir que a interface seja atualizada entre as adições de arquivos
                QCoreApplication.processEvents()

            # Após adicionar todos os arquivos, resetar a barra de progresso para 0%
            self.ui.addFilesProjectProgress.setValue(0)

        # Reativar o filtro depois que o carregamento de arquivos for concluído
        self.ui.filterFilesEdit.setEnabled(True)

    def is_file_in_list(self, file_path):
        """
        Verifica se um arquivo com o mesmo caminho já está presente na lista.
        """
        for i in range(self.ui.attachmentsList.count()):
            item_widget = self.ui.attachmentsList.itemWidget(self.ui.attachmentsList.item(i))
            if item_widget.file_path == file_path:
                return True  # Arquivo já existe na lista
        return False  # Arquivo não encontrado



    def filter_files(self):
        """
        Filtra os arquivos na lista com base no texto do QLineEdit.
        """
        filter_text = self.ui.filterFilesEdit.text().lower()  # Texto digitado, convertido para minúsculo
        self.ui.clearFilterProjectButton.clicked.connect(lambda: self.clear_filter())
        # Iterar sobre todos os itens na lista
        for i in range(self.ui.attachmentsList.count()):
            item_widget = self.ui.attachmentsList.itemWidget(self.ui.attachmentsList.item(i))

            # Obter os dados de cada arquivo: nome, formato e tamanho
            file_name = item_widget.file_name_label.text().lower()
            file_format = item_widget.file_format_label.text().lower()
            file_size = item_widget.file_size_label.text().lower()

            # Verifique se o texto do filtro está contido no nome, formato ou tamanho
            if (filter_text in file_name) or (filter_text in file_format) or (filter_text in file_size):
                self.ui.attachmentsList.item(i).setHidden(False)  # Mostrar item
            else:
                self.ui.attachmentsList.item(i).setHidden(True)  # Esconder item

    def clear_filter(self):
        self.ui.filterFilesEdit.setText("")

    def update_file(self, index, new_file_path):
        """
        Atualiza um arquivo existente na lista de anexos com a seleção de um novo diretório de arquivos.
        """
        # Obter o item da lista pelo índice
        item_widget = self.ui.attachmentsList.itemWidget(self.ui.attachmentsList.item(index))
        
        # Mostrar a caixa de diálogo para selecionar o novo arquivo
        new_file, _ = QFileDialog.getOpenFileName(None, "Edit File", "", "All Files (*)")
        if new_file:
            # Extraia informações do novo arquivo
            file_name = os.path.basename(new_file)
            file_format = os.path.splitext(file_name)[1].lstrip(".") or 'None'
            file_size = round(os.path.getsize(new_file) / 1024, 2)  # Tamanho em KB

            # Atualizar os labels do widget
            item_widget.file_name_label.setText(file_name)
            item_widget.file_format_label.setText(file_format)
            item_widget.file_size_label.setText(f"{file_size} KB")

            # Atualizar a label de caminho com o novo file_path
            item_widget.file_path_label.setText(new_file)

            # Atualizar o caminho do arquivo armazenado no widget
            item_widget.file_path = new_file


    def remove_file(self, index):
        """
        Remove um arquivo da lista de anexos.
        """
        # Obter o item da lista pelo índice
        list_item = self.ui.attachmentsList.item(index)

        if list_item:
            row = self.ui.attachmentsList.row(list_item)
            self.ui.attachmentsList.takeItem(row)

            # Atualizar os índices dos itens restantes
            for i in range(self.ui.attachmentsList.count()):
                item_widget = self.ui.attachmentsList.itemWidget(self.ui.attachmentsList.item(i))
                item_widget.index_label.setText(f"{i + 1}")


    def connect_file_item_buttons(self, file_list_widget, edit_button, delete_button, index):
        """
        Conecta os botões 'Edit' e 'Delete' às funções de edição e exclusão.
        """
        def edit_file():
            new_file, _ = QFileDialog.getOpenFileName(None, "Edit File", "", "All Files (*)")
            if new_file:
                self.update_file(index - 1, new_file)

        def delete_file():
            self.remove_file(index - 1)

        edit_button.clicked.connect(edit_file)
        delete_button.clicked.connect(delete_file)
