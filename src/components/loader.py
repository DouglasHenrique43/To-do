from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QTimer, QEventLoop
from PySide6.QtGui import QPainter, QColor, QPen

class CircularLoader(QWidget):
    def __init__(self, size=300, line_width=2, line_color="#3498db", arc_length=120, is_determinate=True, speed=5, ui=None):
        super().__init__()

        self.ui = ui  # Referência ao UI do MainWindow
        self.setWindowTitle("Loader Circular Personalizado")
        self.setFixedSize(size, size)  # Mantém dimensões fixas para um círculo perfeito

        # Parâmetros configuráveis
        self.line_width = line_width
        self.line_color = QColor(line_color)
        self.arc_length = arc_length * 16  # Conversão para formato usado por QPainter
        self.angle = 0
        self.progress = 0  # Progresso inicial (0%)
        self.is_determinate = is_determinate  # Define o comportamento do loader
        self.speed = speed  # Velocidade de rotação (graus por passo)

        # Criando o loop de eventos
        self.event_loop = QEventLoop(self)

        # Timer para animação
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_angle)
        self.timer.start(16)  # Atualiza a cada 16 ms para ~60 FPS

        # Tela escurecida (overlay)
        self.overlay = QWidget(self.ui.centralwidget)  # Widget de sobreposição, posicionado dentro do centralwidget
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 0.7);")  # Cor de fundo semi-transparente
        self.overlay.setGeometry(0, 0, self.ui.centralwidget.width(), self.ui.centralwidget.height())
        self.overlay.show()

        # Loader centralizado
        self.setParent(self.overlay)  # O loader será filho do overlay
        self.move(
            (self.ui.centralwidget.width() - self.width()) // 2, 
            (self.ui.centralwidget.height() - self.height()) // 2
        )
        self.show()

        # Exibe a tela escurecida e o loader
        self.show_overlay(True)

    def update_angle(self):
        if self.is_determinate:
            # Incrementa o progresso até 100%
            self.progress += 0.5  # Incremento menor para suavidade
            if self.progress >= 100:
                self.progress = 100  # Trava no máximo
                self.timer.stop()  # Para o timer, finalizando a animação
                self.show_overlay(False)  # Esconde o overlay
                self.hide()  # Esconde o loader
                self.event_loop.quit()  # Finaliza o loop de eventos
        else:
            # Comportamento de rotação infinita
            self.angle += self.speed * 0.3  # Incremento ajustado para suavidade
            if self.angle >= 360:
                self.angle = 0
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Configuração de um quadrado perfeito para desenhar o círculo
        rect = self.rect().adjusted(
            self.line_width, self.line_width,
            -self.line_width, -self.line_width
        )

        # Configurações do pincel
        pen = QPen(self.line_color)
        pen.setWidth(self.line_width)
        painter.setPen(pen)

        if self.is_determinate:
            # Calcula o arco baseado no progresso
            arc_length = int((self.progress / 100) * 360) * 16  # Progresso em graus
            painter.drawArc(rect, 90 * 16, arc_length)  # Início no sentido vertical (90°)
        else:
            # Desenha o arco rotativo (infinito)
            painter.drawArc(rect, self.angle * 16, self.arc_length)

        painter.end()

    def show_overlay(self, show):
        # Mostra ou esconde o overlay (tela escurecida)
        if show:
            self.overlay.show()
        else:
            self.overlay.hide()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Atualiza a posição do loader quando a janela for redimensionada
        self.overlay.setGeometry(0, 0, self.ui.centralwidget.width(), self.ui.centralwidget.height())
        self.move(
            (self.ui.centralwidget.width() - self.width()) // 2, 
            (self.ui.centralwidget.height() - self.height()) // 2
        )

    def start(self):
        # Inicia o loop de eventos, bloqueando a execução até o carregamento ser concluído
        self.event_loop.exec_()
