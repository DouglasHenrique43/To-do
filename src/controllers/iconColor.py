from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor
from PySide6.QtSvg import QSvgRenderer
import os

# Função que altera a cor de todos os ícones passados na lista
def alter_icons_color(icons_list, color: str, size: QSize = QSize(24, 24)):
    """
    Modifica a cor de preenchimento dos ícones SVG fornecidos na lista.

    :param icons_list: Lista de nomes de ícones (sem o caminho completo).
    :param color: Cor a ser aplicada no preenchimento (em formato hexadecimal: "#RRGGBB").
    :param size: Tamanho do ícone (opcional, padrão é 24x24).
    :return: Dicionário com os ícones alterados.
    """
    prefix = ":/icons/icons/"
    icons = {}

    for icon_name in icons_list:
        icon_path = f"{prefix}{icon_name}.svg"  # Caminho completo do ícone
        icon = _alter_svg_fill(icon_path, color, size)  # Altera a cor do ícone
        icons[icon_name] = icon  # Armazena o ícone alterado no dicionário

    return icons

def _alter_svg_fill(svg_path: str, color: str, size: QSize = QSize(24, 24)) -> QIcon:
    """
    Altera a cor de preenchimento de um ícone SVG específico e retorna o ícone modificado.

    :param svg_path: Caminho completo do arquivo SVG.
    :param color: Cor a ser aplicada no preenchimento (em formato hexadecimal).
    :param size: Tamanho do ícone (opcional, padrão é 24x24).
    :return: QIcon modificado.
    """
    # Carregar o SVG
    renderer = QSvgRenderer(svg_path)
    pixmap = QPixmap(size)
    pixmap.fill(Qt.transparent)  # Preenche o fundo com transparência

    # Criar um pintor para renderizar o SVG
    painter = QPainter(pixmap)
    renderer.render(painter)

    # Aplicar a cor de preenchimento
    painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
    painter.fillRect(pixmap.rect(), QColor(color))  # Preenche com a cor especificada
    painter.end()

    # Retornar o ícone modificado
    return QIcon(pixmap)
