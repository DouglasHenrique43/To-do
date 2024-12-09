from PySide6.QtCore import QCoreApplication

# shortcuts.py
class Shortcuts:
    def __init__(self, MainWindow):
        self.ui = MainWindow
        self.setup_shortcuts()

    def setup_shortcuts(self):
        # Atalho Ctrl+Q para fechar a aplicação
        
        # NAVBAR BUTTONS
        self.ui.minimizeAppBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Q", None))
        self.ui.max_resizeButton.setShortcut(QCoreApplication.translate("MainWindow", u"M", None))
        self.ui.closeAppBtn.setShortcut(QCoreApplication.translate("MainWindow", u"ESC", None))

        # LEFT BAR BUTTONS
        self.ui.toggleButton.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
        self.ui.homeButton.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
        self.ui.socialButton.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
        self.ui.projectButton.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
        self.ui.taskButton.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
        self.ui.calendarButton.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
        self.ui.profileButton.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
        self.ui.settingsButton.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))

