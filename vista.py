from PySide6 import QtWidgets
from ui.peliculas import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._setup_ui()

    def _setup_ui(self):
        self.setupUi(self)
