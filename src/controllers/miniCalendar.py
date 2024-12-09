from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout, QLabel, QPushButton
from PySide6.QtCore import QDate, Qt
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR')  # Para Linux/Mac

class CalendarLogic:
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow  # Armazena a referência para a janela principal.
        
        # Atribui o widget QLabel de exibição do mês e ano à variável 'monthLabel'.
        self.month_Label = self.MainWindow.monthLabel
        self.day_Label = self.MainWindow.dayLabel
        # Inicializa o mês e ano atual
        self.current_date = datetime.now()

        # Canvas para o calendário
        self.canvas_calendar = self.MainWindow.canvasCalendar
        
        # Inicializa o calendário
        self.update_month_label()
        self.update_calendar()  # Atualiza o calendário logo após a inicialização

    def update_month_label(self):
        """
        Atualiza o QLabel com o nome abreviado do mês atual e o ano.
        """
        month = self.current_date.strftime('%B')  # Nome abreviado do mês
        year = self.current_date.year
        day_of_week = self.current_date.strftime('%A')
        month = month.capitalize()  # Mês com a primeira letra maiúscula
        day_of_week = day_of_week.capitalize()  # Dia da semana com a primeira letra maiúscula
        self.month_Label.setText(f'{month} {year} - {day_of_week}')
        
    def update_calendar(self):
        """
        Atualiza o calendário com os dias do mês atual.
        """
        # Limpa o layout existente
        layout = self.canvas_calendar.layout()
        if layout:
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if widget is not None:
                    widget.deleteLater()  # Limpa o layout existente

        # Cria um novo layout para o calendário
        grid_layout = QGridLayout()
        self.canvas_calendar.setLayout(grid_layout)  # Define o layout para o canvas_calendar

        # Define o primeiro dia do mês atual
        first_day_of_month = QDate(self.current_date.year, self.current_date.month, 1)
        first_day_weekday = first_day_of_month.dayOfWeek() - 1  # Ajuste: 0 (Domingo) até 6 (Sábado)
        days_in_month = first_day_of_month.daysInMonth()

        # Adiciona os dias da semana (com estilo para centralizar e alinhamento uniforme)
        days_of_week = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']
        for col, day in enumerate(days_of_week):
            day_label = QLabel(day)
            day_label.setAlignment(Qt.AlignCenter)  # Alinha o texto ao centro
            grid_layout.addWidget(day_label, 0, col)
            grid_layout.setColumnStretch(col, 1)  # Garante que cada coluna tenha a mesma largura

        # Adiciona os botões para os dias do mês
        row = 1
        col = first_day_weekday
        for day in range(1, days_in_month + 1):
            day_button = QPushButton(str(day))
            
            # Atribui um objectName único para cada botão de dia
            day_button.setObjectName(f"day_{day}")  # Exemplo: "day_1", "day_2", etc.
            day_button.setCursor(Qt.PointingHandCursor)  # Define o cursor como "pointer"
            # Verifica se o dia é o dia atual
            if day == self.current_date.day and self.current_date.month == first_day_of_month.month() and self.current_date.year == first_day_of_month.year():
                day_button.setStyleSheet("border-radius: 17%; font-weight: bold;")  # Estilo para o dia de hoje
                day_button.setObjectName("current_day")  # Adiciona um objectName específico para o dia atual
            else:
                day_button.setStyleSheet("background-color: transparent; font-weight: bold")  # Estilo normal
            
            day_button.setFixedSize(35, 35)
            day_button.clicked.connect(lambda checked, day=day: self.on_day_click(day))

            # Adiciona o botão ao layout, e ajusta a coluna
            grid_layout.addWidget(day_button, row, col)
            grid_layout.setColumnStretch(col, 1)  # Garante que a largura das colunas se ajustem

            col += 1
            if col > 6:  # Se passar do sábado, vai para a próxima linha
                col = 0
                row += 1

    def on_day_click(self, day):
        """
        Manipula o clique de um dia no calendário.
        """
        print(f"Dia selecionado: {day}")
