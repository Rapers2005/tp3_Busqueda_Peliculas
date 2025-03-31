from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Signal, Slot
from ui.peliculas import Ui_PeliculasWindow

class PeliculasWindow(QtWidgets.QMainWindow, Ui_PeliculasWindow):

    buscar_pelicula_signal = Signal(str)
    buscar_actores_signal = Signal(str, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Buscador de Películas")
        self._connect_signals()

    def _connect_signals(self):

        self.pushButton.clicked.connect(self._on_emitir_buscar)

    @Slot()
    def _on_emitir_buscar(self):

        titulo = self.lineEdit.text().strip()
        if titulo:
            self.buscar_pelicula_signal.emit(titulo)
        else:
            actor1 = self.TituloActores.text().strip()
            actor2 = self.TituloActores_2.text().strip()
            self.buscar_actores_signal.emit(actor1, actor2)


    def configurar_completers(self, lista_titulos, lista_actores):
        from PySide6.QtWidgets import QCompleter
        completer_titulo = QCompleter(lista_titulos, self)
        completer_titulo.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.lineEdit.setCompleter(completer_titulo)

        completer_actor_1 = QCompleter(lista_actores, self)
        completer_actor_2 = QCompleter(lista_actores, self)
        completer_actor_1.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        completer_actor_2.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.TituloActores.setCompleter(completer_actor_1)
        self.TituloActores_2.setCompleter(completer_actor_2)

    def limpiar_interfaz(self):
        self.lineEdit.clear()
        self.TituloActores.clear()
        self.TituloActores_2.clear()

    def mostrar_mensaje(self, mensaje):
        QtWidgets.QMessageBox.information(self, "Información", mensaje)


    def actualizar_poster(self, ruta_imagen):
        pixmap = QPixmap(ruta_imagen)
        if not pixmap.isNull():
            self.labelPoster.setPixmap(
                pixmap.scaled(
                    self.labelPoster.size(),
                    QtCore.Qt.KeepAspectRatio,
                    QtCore.Qt.SmoothTransformation
                )
            )
        else:
            self.labelPoster.setText("Imagen no disponible")
