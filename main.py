import sys
from PySide6 import QtWidgets
from modelo import PeliculasModel  # Asegúrate de que este archivo existe y es accesible
from vista import MainWindow  # Asegúrate de que el archivo de vista está bien importado
from controlador import Controlador  # Asegúrate de que el controlador está bien importado

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()

    modelo = PeliculasModel()

    controlador = Controlador(modelo, window)

    window.show()

    sys.exit(app.exec())
