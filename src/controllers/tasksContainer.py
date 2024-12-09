from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QLabel, QGraphicsBlurEffect
from PySide6.QtCore import Qt

class TasksContainer:
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow  # Armazena a referência para a janela principal.
        
        # Tasks ativas
        self.activeTasks = 0

        # Importando Titulo da sessão
        self.tasks_label = self.MainWindow.tasksLabel
        

    def addTask(self):
        """
        Adiciona uma tarefa à lista de tarefas.
        """



        # Atualiza o título da sessão
        self.tasks_label.setText(f"My Tasks <span style='font-size: 12px;'>({self.activeTasks})</span>")
