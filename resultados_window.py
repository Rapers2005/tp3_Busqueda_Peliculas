from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QPixmap
from ui_peliculas2 import Ui_PeliculasWindow

class ResultadosWindow(QtWidgets.QMainWindow, Ui_PeliculasWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Resultados de la Búsqueda")

        self.pushButton.clicked.connect(self.close)

    def mostrar_resultados(self, peliculas, busqueda_por_titulo=True):


        self.Peliculas.clearContents()
        self.PeliculasComunes.clearContents()

        self.Peliculas.setRowCount(5)
        self.Peliculas.setColumnCount(1)

        self.PeliculasComunes.setRowCount(2)
        self.PeliculasComunes.setColumnCount(1)

        if not peliculas:
            return

        if busqueda_por_titulo:
            pelicula = peliculas[0]

            self.Peliculas.setItem(0, 0, QtWidgets.QTableWidgetItem(
                pelicula.get('titulo', '')
            ))

            actores_dicts = pelicula.get('actores', [])
            nombres_actores = [actor_dict.get("nombre", "Desconocido") for actor_dict in actores_dicts]
            self.Peliculas.setItem(1, 0, QtWidgets.QTableWidgetItem(
                ', '.join(nombres_actores)
            ))

            self.Peliculas.setItem(2, 0, QtWidgets.QTableWidgetItem(
                pelicula.get('sinopsis', '')
            ))

            puntuacion = str(pelicula.get('puntuacion', 'N/A'))
            self.Peliculas.setItem(3, 0, QtWidgets.QTableWidgetItem(puntuacion))

            duracion = str(pelicula.get('duracion', 'N/A'))
            self.Peliculas.setItem(4, 0, QtWidgets.QTableWidgetItem(duracion))

            ruta_poster = pelicula.get('ruta_poster')
            if ruta_poster:
                pixmap = QPixmap(ruta_poster)
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
            else:
                self.labelPoster.setText("Sin póster")

        else:

            lista_titulos = [p["titulo"] for p in peliculas]
            lista_anios = [str(p.get("anio", "N/A")) for p in peliculas]

            self.PeliculasComunes.setItem(0, 0, QtWidgets.QTableWidgetItem(
                ', '.join(lista_titulos)
            ))
            self.PeliculasComunes.setItem(1, 0, QtWidgets.QTableWidgetItem(
                ', '.join(lista_anios)
            ))

            self.labelPoster.clear()
            self.labelPoster.setText("")

    def limpiar(self):

        self.Peliculas.clearContents()
        self.PeliculasComunes.clearContents()
        self.labelPoster.clear()
