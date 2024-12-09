from src.main import MainWindow
from config.appSetings import *
from src.controllers.custom_grips import *

from PySide6.QtCore import QPropertyAnimation, QEasingCurve, Qt, QParallelAnimationGroup, QEvent, QTimer
from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QSizeGrip, QPushButton, QGraphicsDropShadowEffect

# Variáveis globais
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True
ENABLE_CUSTOM_TITLE_BAR = True


class UIFunctions(MainWindow):
    # ====================================================
    # Funções de Maximizar/Restaurar
    # ====================================================

    def maximize_restore(self):
        """
        Alterna entre maximizar e restaurar a janela.
        """
        global GLOBAL_STATE
        if not self.ui:  # Verifica se self.ui é None
            return

        if not GLOBAL_STATE:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.max_resizeButton.setIcon(QIcon(u":/icons/icons/icon_restore.png"))
            self.ui.frame_size_grip.hide()  # Oculta o grip de redimensionamento
            self.left_grip.hide()  # Oculta o grip esquerdo
            self.right_grip.hide()  # Oculta o grip direito
            self.top_grip.hide()  # Oculta o grip superior
            self.bottom_grip.hide()  # Oculta o grip inferior
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.max_resizeButton.setIcon(QIcon(u":/icons/icons/icon_maximize.png"))
            self.ui.frame_size_grip.show()  # Mostra o grip de redimensionamento
            self.left_grip.show()  # Mostra o grip esquerdo
            self.right_grip.show()  # Mostra o grip direito
            self.top_grip.show()  # Mostra o grip superior
            self.bottom_grip.show()  # Mostra o grip inferior

    # RETURN STATUS
    # ///////////////////////////////////////////////////////////////
    def returStatus(self):
        return GLOBAL_STATE

    # SET STATUS
    # ///////////////////////////////////////////////////////////////
    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status


    # ====================================================
    # Funções de Animação
    # ====================================================

    def toggleMenu(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # TOGGLE LEFT BOX
    # ///////////////////////////////////////////////////////////////
    def toggleLeftBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraLeftBox.width()
            widthRightBox = self.ui.extraRightBox.width()
            maxExtend = Settings.LEFT_BOX_WIDTH
            color = Settings.BTN_LEFT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.settingsButton.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.settingsButton.setStyleSheet(style + color)
                if widthRightBox != 0:
                    style = self.ui.settingsTopBtn.styleSheet()
                    self.ui.settingsTopBtn.setStyleSheet(style.replace(Settings.BTN_RIGHT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.settingsButton.setStyleSheet(style.replace(color, ''))
                
        UIFunctions.start_box_animation(self, width, widthRightBox, "left")

    # TOGGLE RIGHT BOX
    # ///////////////////////////////////////////////////////////////
    def toggleRightBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraRightBox.width()
            widthLeftBox = self.ui.extraLeftBox.width()
            maxExtend = Settings.RIGHT_BOX_WIDTH
            color = Settings.BTN_RIGHT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.settingsTopBtn.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.settingsTopBtn.setStyleSheet(style + color)
                if widthLeftBox != 0:
                    style = self.ui.settingsButton.styleSheet()
                    self.ui.settingsButton.setStyleSheet(style.replace(Settings.BTN_LEFT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.settingsTopBtn.setStyleSheet(style.replace(color, ''))

            UIFunctions.start_box_animation(self, widthLeftBox, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0 

        # Check values
        if left_box_width == 0 and direction == "left":
            left_width = 240
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = 240
        else:
            right_width = 0       

        # ANIMATION LEFT BOX        
        self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX        
        self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(Settings.TIME_ANIMATION)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    def toggle_box(self, box, button, max_width, color):
        """
        Lógica genérica para alternar caixas laterais.
        """
        width = box.width()
        widthExtended = max_width if width == 0 else 0

        style = button.styleSheet()
        button.setStyleSheet(style + color if width == 0 else style.replace(color, ""))

        # Animação da caixa
        self.animation = QPropertyAnimation(box, b"minimumWidth")
        self.animation.setDuration(Settings.TIME_ANIMATION)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    # SELECT/DESELECT MENU
    # ///////////////////////////////////////////////////////////////
    # SELECT
    def selectMenu(getStyle):
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select
    
    # DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    # START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    # RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))


    # ====================================================
    # Configurações de UI e Título
    # ====================================================

    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))
        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            #STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if UIFunctions.returStatus(self):
                    UIFunctions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
            self.ui.titleRightInfo.mouseMoveEvent = moveWindow

            # CUSTOM GRIPS
            self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
            self.right_grip = CustomGrip(self, Qt.RightEdge, True)
            self.top_grip = CustomGrip(self, Qt.TopEdge, True)
            self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        else:
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

    def create_grips(self):
        """
        Cria grips para redimensionamento.
        """
        self.ui.left_grip = CustomGrip(self.ui, Qt.LeftEdge, True)
        self.ui.right_grip = CustomGrip(self.ui, Qt.RightEdge, True)
        self.ui.top_grip = CustomGrip(self.ui, Qt.TopEdge, True)
        self.ui.bottom_grip = CustomGrip(self.ui, Qt.BottomEdge, True)

    def disableCustomTitleBar(self):
        """
        Configurações caso barra de título customizada esteja desabilitada.
        """
        self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
        self.ui.minimizeAppBtn.hide()
        self.ui.maximizeRestoreAppBtn.hide()
        self.ui.closeAppBtn.hide()
        self.ui.frame_size_grip.hide()

    def applyShadow(self):
        """
        Aplica sombra na janela principal.
        """
        shadow = QGraphicsDropShadowEffect(self.ui)
        shadow.setBlurRadius(17)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(shadow)

    # ====================================================
    # Eventos de Redimensionamento
    # ====================================================

    def resize_grips(self):
        if Settings.ENABLE_CUSTOM_TITLE_BAR and not GLOBAL_STATE:  # Verifica se não está maximizado
            self.left_grip.setGeometry(0, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            self.top_grip.setGeometry(0, 0, self.width(), 10)
            self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)
        else:
            # Se maximizado, oculte os grips
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()

    # ====================================================
    # Shadow Efect
    # ====================================================

    def apply_shadow(self, widget, color, blur_radius=15, offset_x=0, offset_y=0):
        """
        Aplica uma sombra a um widget.

        :param widget: O widget (item) ao qual a sombra será aplicada.
        :param color: A cor da sombra (objeto QColor ou string representando a cor, como '#000000').
        """
        self.person_shadow = QGraphicsDropShadowEffect(self)
        self.person_shadow.setBlurRadius(blur_radius)
        self.person_shadow.setXOffset(offset_x)
        self.person_shadow.setYOffset(offset_y)
        self.person_shadow.setColor(QColor(*color))
        widget.setGraphicsEffect(self.person_shadow)
