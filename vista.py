from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from ui.peliculas import Ui_MainWindow

from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from ui.peliculas import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._setup_ui()

    def _setup_ui(self):
        self.setupUi(self)

    @Slot(str)
    def set_movie_title(self, title):
        self.lineEdit.setText(title)

    @Slot(str)
    def set_actor1(self, actor):
        self.lineEdit_3.setText(actor)

    @Slot(str)
    def set_actor2(self, actor):
        self.lineEdit_4.setText(actor)

    def conectar_boton_cargar_json(self, funcion):
        self.pushButtonCargarJSON.clicked.connect(funcion)

    def obtener_titulo(self):
        return self.lineEdit.text()

    def obtener_actor1(self):
        return self.lineEdit_3.text()

    def obtener_actor2(self):
        return self.lineEdit_4.text()


