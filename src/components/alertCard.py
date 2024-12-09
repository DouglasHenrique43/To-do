from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGraphicsOpacityEffect, QFrame, QPushButton
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QTimer, QPoint
from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor
from PySide6.QtSvg import QSvgRenderer

class AlertWidget(QWidget):
    alert_active = None  # Variável de controle para o alerta ativo

    def __init__(self, parent: QWidget, background_color: str, strong_color: str, icon_path: str, message: str, y_position: int = 30, x_position: int = None):
        # Se já houver um alerta ativo, chama o fade_out no alerta anterior antes de criar um novo
        if AlertWidget.alert_active:
            AlertWidget.alert_active.fade_out(immediate=True)  # Fecha o alerta anterior imediatamente

        super().__init__(parent)

        # Define o alerta atual como ativo
        AlertWidget.alert_active = self  # Marca o alerta como ativo

        self.setStyleSheet(""" 
            padding: 0;
            margin: 0;
            QPushButton, QLabel {
                border: none;
            }
        """)

        self.setFixedWidth(400)  # Largura fixa do widget
        self.setFixedHeight(70)  # Altura fixa do widget
        self.setStyleSheet("padding: 0; margin: 0;")  # Remover margens do widget para melhor controle

        # Criando o QFrame como o frame pai do alerta
        self.frame = QFrame(self)
        self.frame.setStyleSheet(f"""
            QFrame {{
                background-color: {background_color};
                color: {strong_color};
                font-weight: bold;
                border-left: 4px solid {strong_color};  /* Definindo a borda esquerda com a cor forte */
                border-top-right-radius: 3px;  /* Borda arredondada no canto superior direito */
                border-bottom-right-radius: 3px;  /* Borda arredondada no canto inferior direito */
                padding: 0;
                margin: 0;
            }}
        """)
        self.frame.setFixedHeight(70)  # Altura do QFrame

        # Criando um QWidget para evitar que os filhos herdem o estilo do QFrame
        self.content_widget = QWidget(self.frame)
        self.content_widget.setStyleSheet("margin-left: 10px; margin-right: 10px; background-color: transparent; border: transparent;")  # Definir margem para o conteúdo
        self.content_layout = QHBoxLayout(self.content_widget)
        self.content_layout.setAlignment(Qt.AlignVCenter)  # Alinhando verticalmente no centro
        self.content_layout.setContentsMargins(0, 0, 0, 0)  # Sem margens externas
        self.content_layout.setSpacing(10)  # Definir espaçamento entre os elementos

        # Adicionando ícone à esquerda
        if icon_path:
            icon_label = QLabel(self.content_widget)
            icon_pixmap = self.modify_icon_color(icon_path, strong_color)
            icon_label.setPixmap(icon_pixmap)
            icon_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            icon_label.setStyleSheet("margin-right: 10px; border: transparent; background-color: transparent;")
            self.content_layout.addWidget(icon_label)

        # Criando e nomeando a label para o conteúdo da mensagem
        self.message_label = QLabel(message, self.content_widget)
        self.message_label.setStyleSheet("font-family: Arial; font-size: 13px;")

        self.content_layout.addWidget(self.message_label)

        # Adicionando o botão de fechar com ícone modificado
        self.close_button = QLabel(self.content_widget)
        self.close_button.setCursor(Qt.PointingHandCursor)
        self.close_button.setStyleSheet("margin: 0; border: transparent; background-color: transparent;")
        
        close_icon_pixmap = self.modify_icon_color(r'src\assets\icons\x.svg', strong_color)
        self.close_button.setPixmap(close_icon_pixmap)  # Definir o ícone de fechamento com a cor modificada
        
        self.close_button.setStyleSheet("border: transparent; background-color: transparent;")
        self.close_button.setAlignment(Qt.AlignRight)
        self.close_button.mousePressEvent = self.close_alert  # Chama a animação de fechamento ao clicar
        self.content_layout.addWidget(self.close_button)

        # Layout do QFrame
        frame_layout = QVBoxLayout(self.frame)
        frame_layout.setContentsMargins(0, 0, 0, 0)
        frame_layout.setSpacing(0)
        frame_layout.addWidget(self.content_widget)

        # Efeito de opacidade
        self.effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.effect)
        self.effect.setOpacity(0)

        # Calculando a posição X para centralizar horizontalmente
        window_geometry = parent.geometry()
        screen_width = window_geometry.width()
        self.alerts_x_position = (screen_width - self.width()) // 2

        # Se a posição Y não for especificada, centraliza verticalmente
        if y_position == -1:
            screen_height = window_geometry.height()
            self.alerts_y_position = (screen_height - self.height()) // 2
        else:
            self.alerts_y_position = y_position

        # Inicializando a posição
        self.move(self.alerts_x_position, self.alerts_y_position)

        # Animação de opacidade e movimento de queda
        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setEasingCurve(QEasingCurve.OutQuad)

        self.position_animation = QPropertyAnimation(self, b"pos")
        self.position_animation.setDuration(1000)
        self.position_animation.setStartValue(QPoint(self.x(), y_position))
        self.position_animation.setEndValue(QPoint(self.x(), y_position + 50))
        self.position_animation.setEasingCurve(QEasingCurve.OutQuad)

        self.animation.start()
        self.position_animation.start()

        # Timer para esconder o alerta após 6 segundos
        self.fade_out_timer = QTimer(self)
        self.fade_out_timer.setSingleShot(True)
        self.fade_out_timer.timeout.connect(self.fade_out)
        self.fade_out_timer.start(3000)

    def modify_icon_color(self, icon_path: str, color: str, size: int = 26) -> QPixmap:
        renderer = QSvgRenderer(icon_path)

        pixmap = QPixmap(size, size)
        pixmap.fill(Qt.transparent)

        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()

        painter.begin(pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), QColor(color))
        painter.end()

        return pixmap

    def fade_out(self, immediate=False):
        if immediate:
            self.close_and_unlock()
            return

        self.fade_out_animation = QPropertyAnimation(self.effect, b"opacity")
        self.fade_out_animation.setDuration(1000)
        self.fade_out_animation.setStartValue(1)
        self.fade_out_animation.setEndValue(0)
        self.fade_out_animation.setEasingCurve(QEasingCurve.InQuad)

        self.fade_out_position_animation = QPropertyAnimation(self, b"pos")
        self.fade_out_position_animation.setDuration(1000)
        self.fade_out_position_animation.setStartValue(self.pos())
        self.fade_out_position_animation.setEndValue(QPoint(self.x(), self.y() - 50))

        self.fade_out_animation.start()
        self.fade_out_position_animation.start()

        self.fade_out_animation.finished.connect(self.close_and_unlock)

    def close_and_unlock(self):
        self.close()  # Fecha o widget
        AlertWidget.alert_active = None  # Libera a criação de novos alertas

    def close_alert(self, event=None):
        self.fade_out_timer.stop()  # Para o timer de fade out
        self.fade_out()  # Inicia a animação de fade out ao clicar no botão de fechar
