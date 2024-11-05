from PySide6 import QtWidgets
from PySide6.QtCore import Slot, Signal
from ui.peliculas import Ui_PeliculasWindow

class PeliculasWindow(QtWidgets.QMainWindow, Ui_PeliculasWindow):
    buscar_pelicula_signal = Signal(str)
    buscar_actores_signal = Signal(str, str)

    def __init__(self):
        super(PeliculasWindow, self).__init__()
        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self):
        self.setupUi(self)

    def _connect_signals(self):
        self.pushButton.clicked.connect(self._on_buscar_pelicula)
        self.pushButton_2.clicked.connect(self._on_buscar_actores)

    @Slot()
    def _on_buscar_pelicula(self):
        titulo = self.obtener_titulo()
        self.buscar_pelicula_signal.emit(titulo)

    @Slot()
    def _on_buscar_actores(self):
        actor1 = self.obtener_actor1()
        actor2 = self.obtener_actor2()
        self.buscar_actores_signal.emit(actor1, actor2)

    @Slot(str)
    def set_movie_title(self, title):
        self.lineEdit.setText(title)

    @Slot(str)
    def set_actor1(self, actor):
        self.lineEdit_3.setText(actor)

    @Slot(str)
    def set_actor2(self, actor):
        self.lineEdit_4.setText(actor)

    def obtener_titulo(self):
        return self.lineEdit.text()

    def obtener_actor1(self):
        return self.lineEdit_3.text()

    def obtener_actor2(self):
        return self.lineEdit_4.text()

    @Slot(list)
    def actualizar_tabla_peliculas(self, peliculas):
        self.Peliculas.setRowCount(len(peliculas))
        for row, pelicula in enumerate(peliculas):
            self.Peliculas.setItem(row, 0, QtWidgets.QTableWidgetItem(pelicula['titulo']))
            self.Peliculas.setItem(row, 1, QtWidgets.QTableWidgetItem(', '.join(pelicula['actores'])))
            self.Peliculas.setItem(row, 2, QtWidgets.QTableWidgetItem(pelicula['sinopsis']))
            self.Peliculas.setItem(row, 3, QtWidgets.QTableWidgetItem(str(pelicula['puntuacion'])))
            self.Peliculas.setItem(row, 4, QtWidgets.QTableWidgetItem(str(pelicula.get('duracion', 'N/A'))))

    @Slot(list)
    def actualizar_tabla_peliculas_comunes(self, peliculas):
        self.PeliculasComunes.setRowCount(len(peliculas))
        for row, pelicula in enumerate(peliculas):
            self.PeliculasComunes.setItem(row, 0, QtWidgets.QTableWidgetItem(pelicula['titulo']))
            self.PeliculasComunes.setItem(row, 1, QtWidgets.QTableWidgetItem(str(pelicula.get('anio', 'N/A'))))

    @Slot(str)
    def mostrar_mensaje(self, mensaje):
        QtWidgets.QMessageBox.information(self, "Información", mensaje)

    @Slot(str)
    def actualizar_poster(self, ruta_imagen):
        pixmap = QtWidgets.QPixmap(ruta_imagen)
        if not pixmap.isNull():
            self.labelPoster.setPixmap(pixmap.scaled(self.labelPoster.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        else:
            self.labelPoster.setText("Imagen no disponible")