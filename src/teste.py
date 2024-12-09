from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPainter, QColor, QPen


class CircularLoader(QWidget):
    def __init__(self, size=300, line_width=10, line_color="#3498db", arc_length=120, is_determinate=False, speed=5):
        super().__init__()
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

        # Label para exibir a porcentagem
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50;")
        self.label.setGeometry(0, 0, size, size)

        # Timer para animação
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_angle)
        self.timer.start(16)  # Atualiza a cada 16 ms para ~60 FPS

    def update_angle(self):
        if self.is_determinate:
            # Incrementa o progresso até 100%
            self.progress += 0.5  # Incremento menor para suavidade
            if self.progress > 100:
                self.progress = 100  # Trava no máximo
            # Atualiza o texto do label com o progresso atual
            self.label.setText(f"{int(self.progress)}%")
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


# Função para configurar e criar o loader
def create_circular_loader(
    parent=None, size=300, line_width=10, line_color="#3498db", arc_length=120, is_determinate=False, speed=5
):
    loader = CircularLoader(size, line_width, line_color, arc_length, is_determinate, speed)
    loader.setParent(parent)
    return loader


if __name__ == "__main__":
    app = QApplication([])

    # Loader indeterminado (comportamento rotativo infinito)
    loader_infinite = create_circular_loader(
        size=300,  # Tamanho fixo do círculo
        line_width=3,
        line_color="#2ecc71",
        arc_length=50,
        is_determinate=False,  # Loader infinito
        speed=15  # Velocidade configurável
    )
    loader_infinite.setWindowTitle("Loader Infinito")
    loader_infinite.show()

    # Loader determinado (simula progresso)
    loader_determinate = create_circular_loader(
        size=300,  # Tamanho fixo do círculo
        line_width=8,
        line_color="#3498db",
        arc_length=100,
        is_determinate=True,  # Loader fixo com progresso
        speed=0  # Ignorado no modo determinado
    )
    loader_determinate.setWindowTitle("Loader Determinado")
    loader_determinate.show()

    app.exec()
