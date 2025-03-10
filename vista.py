from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QPixmap
from ui.peliculas import Ui_PeliculasWindow

class PeliculasWindow(QtWidgets.QMainWindow, Ui_PeliculasWindow):
    # Definimos señales para búsquedas
    buscar_pelicula_signal = Signal(str)
    buscar_actores_signal = Signal(str, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Buscador de Películas")
        self._connect_signals()

    def _connect_signals(self):

        self.pushButton.clicked.connect(self._on_emitir_buscar_pelicula)



    @Slot()
    def _on_emitir_buscar_pelicula(self):
        titulo = self.lineEdit.text().strip()
        self.buscar_pelicula_signal.emit(titulo)

    @Slot()
    def _on_emitir_buscar_actores(self):
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


    def actualizar_tabla_peliculas(self, peliculas):

        self.Peliculas.clearContents()
        self.Peliculas.setRowCount(5)
        self.Peliculas.setColumnCount(1)

        if not peliculas:
            return

        pelicula = peliculas[0]

        self.Peliculas.setItem(0, 0, QtWidgets.QTableWidgetItem(pelicula.get('titulo', '')))

        actores_dicts = pelicula.get('actores', [])

        nombres_actores = [actor_dict['nombre'] for actor_dict in actores_dicts]
        self.Peliculas.setItem(1, 0, QtWidgets.QTableWidgetItem(', '.join(nombres_actores)))
        self.Peliculas.setItem(2, 0, QtWidgets.QTableWidgetItem(pelicula.get('sinopsis', '')))

        puntuacion = str(pelicula.get('puntuacion', 'N/A'))
        self.Peliculas.setItem(3, 0, QtWidgets.QTableWidgetItem(puntuacion))

        duracion = str(pelicula.get('duracion', 'N/A'))
        self.Peliculas.setItem(4, 0, QtWidgets.QTableWidgetItem(duracion))

    def actualizar_tabla_peliculas_comunes(self, peliculas):

        self.PeliculasComunes.clearContents()
        self.PeliculasComunes.setRowCount(2)
        self.PeliculasComunes.setColumnCount(1)

        if not peliculas:
            return

        lista_titulos = [p['titulo'] for p in peliculas]
        lista_anios = [str(p.get('anio', 'N/A')) for p in peliculas]

        str_titulos = ', '.join(lista_titulos)
        str_anios = ', '.join(lista_anios)

        self.PeliculasComunes.setItem(0, 0, QtWidgets.QTableWidgetItem(str_titulos))
        self.PeliculasComunes.setItem(1, 0, QtWidgets.QTableWidgetItem(str_anios))

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
