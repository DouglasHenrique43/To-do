import sys
import os

# Adiciona o diretório pai ao caminho de busca de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtGui import QPalette, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QHeaderView

from components.ui_App import Ui_MainWindow

from theme import *  # Supondo que você tenha um gerenciador de temas
from controllers import *
from utils import *
from components import *
from config.shortCut import *
# Configuração para corrigir problemas de DPI em alta resolução
os.environ["QT_FONT_DPI"] = "96"
GLOBAL_STATE = False

clear()  # Função personalizada para limpar o terminal, se necessário
widgets = None


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "PyDracula - Modern GUI"
        # APPLY TEXTS
        self.setWindowTitle(title)

        # Configuração do tema
        # ///////////////////////////////////////////////////////////////
        self.theme_manager = ThemeManager(self)
        self.theme_manager.set_theme()

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET DECLARATION CLASSES
        # ///////////////////////////////////////////////////////////////
        projectfunc = ProjectFunctions(widgets, self, self.theme_manager.themes[self.theme_manager.palette_name])
        self.shortcuts = Shortcuts(widgets)

        # Cria e exibe o loader e a tela escurecida
        self.loader = CircularLoader

        # SET SHADOW TO OBJECTS
        # ///////////////////////////////////////////////////////////////
        self.setObjectsShadow()


        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)
        
        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.settingsButton.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

    
        # SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.homePage)
        widgets.homeButton.setStyleSheet(UIFunctions.selectMenu(widgets.homeButton.styleSheet()))

        # Conexões de botões
        # ///////////////////////////////////////////////////////////////
        self.setup_topbar_buttons()

        # Adiciona lógicas personalizadas
        # ///////////////////////////////////////////////////////////////
        self.add_custom_logic()
        widgets.homeButton.clicked.connect(self.buttonClick)
        widgets.socialButton.clicked.connect(self.buttonClick)
        widgets.projectButton.clicked.connect(self.buttonClick)
        widgets.taskButton.clicked.connect(self.buttonClick)
        widgets.calendarButton.clicked.connect(self.buttonClick)
        widgets.profileButton.clicked.connect(self.buttonClick)

        # Definindo a posição inicial do primeiro alerta
        self.alert_active = False  # Flag para verificar se um alerta está ativo
        
        window_geometry = self.geometry()
        screen_width = window_geometry.width()

        # Calcula a nova posição do alerta no eixo X
        self.alerts_x_position = screen_width - 400


        self.alerts_y_position = 30

        # Criação do AlertWidget
        self.alert_widget = None

        # Outros ajustes de UI e lógica
        self.setup_ui_and_events()

    # Functions
    # ///////////////////////////////////////////////////////////////
    def add_custom_logic(self):
        mini_calendario = CalendarLogic(self)
        mini_calendario.update_month_label()

        tasks_container = TasksContainer(self)
        tasks_container.addTask()

    def setup_topbar_buttons(self):
        widgets.closeAppBtn.clicked.connect(lambda: self.close())
        widgets.max_resizeButton.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        widgets.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()
        print(f'Botão "{btnName}" clicado!')

        # Lógica para as páginas
        if btnName == "homeButton":
            widgets.stackedWidget.setCurrentWidget(widgets.homePage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        elif btnName == "taskButton":
            widgets.stackedWidget.setCurrentWidget(widgets.dashboardPage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        elif btnName == "socialButton":
            widgets.stackedWidget.setCurrentWidget(widgets.socialPage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        elif btnName == "projectButton":
            widgets.stackedWidget.setCurrentWidget(widgets.projectPage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        elif btnName == "taskButton":
            widgets.stackedWidget.setCurrentWidget(widgets.taskPage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        elif btnName == "calendarButton":
            widgets.stackedWidget.setCurrentWidget(widgets.calendarPage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        elif btnName == "profileButton":
            widgets.stackedWidget.setCurrentWidget(widgets.profilePage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

    def resizeEvent(self, event):
        """Atualiza componentes ao redimensionar a janela."""
        # Atualiza a posição do alerta
        self.update_alert_position()

        # Mantém as funções adicionais de redimensionamento
        UIFunctions.resize_grips(self)
        super().resizeEvent(event)  # Garante que o evento seja tratado pelo pai

    def closeEvent(self, event):
        save_theme(self.theme_manager.palette_name)
        event.accept()

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()


        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            current_page_index = widgets.stackedWidget.currentIndex()
            print(f"A página atual tem o índice: {current_page_index}")

        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
            

    def setup_ui_and_events(self):
        """ Configuração geral da UI e eventos, incluindo botões e temas. """
        # Ajustes de layout e temas
        self.theme_manager = ThemeManager(self)
        self.theme_manager.set_theme()
        UIFunctions.uiDefinitions(self)

        # Botões de navegação
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        self.setObjectsShadow()

    def show_alert(self, background, strong_color, icon_path, message):
        try:
            if self.alert_active:
                return  # Não cria um novo alerta enquanto o anterior não terminar

            # Calcular a posição do alerta
            window_geometry = self.geometry()
            screen_width = window_geometry.width()

            # Cria o AlertWidget com a posição calculada
            self.alert_widget = AlertWidget(
                self, 
                background_color=background, 
                strong_color=strong_color, 
                icon_path=icon_path, 
                message=message,
                y_position=self.alerts_y_position,
                x_position=self.alerts_x_position  # Passa a posição calculada
            )
            
            # Exibe o alerta
            self.alert_widget.show()

        except Exception as e:
            print(f"Ocorreu um erro: {e}")


    def update_alert_position(self):
        """Atualiza a posição do alerta para o centro da janela."""
        if self.alert_widget:
            # Obter a geometria da janela
            window_geometry = self.geometry()
            screen_width = window_geometry.width()
            screen_height = window_geometry.height()

            # Calcula a nova posição do alerta para centralizá-lo
            alert_width = self.alert_widget.width()
            alert_height = self.alert_widget.height()

            # Calcula a posição X e Y para centralizar o alerta
            new_x = (screen_width - alert_width) // 2

            # Atualiza a posição do alerta
            self.alert_widget.move(new_x, self.alert_widget.y())

            
    def on_alert_closed(self):
        """ Método chamado quando o alerta é fechado. """
        self.alert_active = False  # Permite que um novo alerta seja mostrado


    # Shadow effects
    # ///////////////////////////////////////////////////////////////
    def setObjectsShadow(self):
        UIFunctions.apply_shadow(self, widgets.addCategoryProjectButton, (207, 61, 255, 100), blur_radius=50)
        UIFunctions.apply_shadow(self, widgets.newTaskButton, (207, 61, 255, 100), blur_radius=50)

def run_app():
    app = QApplication(sys.argv)
    window = MainWindow()

    # Configurar paleta e janela sem bordas
    palette = QPalette()
    window.setWindowIcon(QIcon(r"src\assets\images\icon.ico"))
    window.setWindowFlags(Qt.FramelessWindowHint) 
    app.setPalette(palette)

    # Exibir a janela maximizada
    #window.showMaximized()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_app()
