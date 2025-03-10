import sys
from PySide6 import QtWidgets
from modelo import PeliculasModel
from vista import PeliculasWindow as MainWindow
from controlador import GestorPeliculas

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    modelo = PeliculasModel()
    controlador = GestorPeliculas(modelo, window)

    window.show()

    sys.exit(app.exec())