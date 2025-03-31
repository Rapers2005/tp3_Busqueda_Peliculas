from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QPixmap
from ui_peliculas2 import Ui_PeliculasWindow

class ResultadosWindow(QtWidgets.QMainWindow, Ui_PeliculasWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Resultados de la Búsqueda")
        self.pushButton.clicked.connect(self.close)

    def mostrar_resultados(self, peliculas, busqueda_por="titulo"):

        if busqueda_por.lower() == "titulo":
            self.labelTituloTitulo2.setText("Por Título")
        else:
            self.labelTituloTitulo2.setText("Por Actores")

        self.Peliculas.clearContents()
        self.Peliculas.setRowCount(5)
        self.Peliculas.setColumnCount(1)

        if not peliculas:
            self._limpiar_poster_container()
            return

        titulos = [p.get("titulo", "") for p in peliculas]
        titulos_comb = ", ".join(titulos)
        self.Peliculas.setItem(0, 0, QtWidgets.QTableWidgetItem(titulos_comb))

        actores_list = []
        for peli in peliculas:
            actores_dicts = peli.get("actores", [])
            nombres_actores = [a.get("nombre", "") for a in actores_dicts]
            actores_list.append(", ".join(nombres_actores))
        actores_comb = " | ".join(actores_list)
        self.Peliculas.setItem(1, 0, QtWidgets.QTableWidgetItem(actores_comb))

        titulos = [p.get("titulo", "") for p in peliculas]
        self.Peliculas.setItem(0, 0, QtWidgets.QTableWidgetItem(", ".join(titulos)))

        sinopsis_list = [p.get("sinopsis", "") for p in peliculas]
        sinopsis_comb = " | ".join(sinopsis_list)
        self.Peliculas.setItem(2, 0, QtWidgets.QTableWidgetItem(sinopsis_comb))

        puntuaciones = [str(p.get("puntuacion", "N/A")) for p in peliculas]
        puntuacion_comb = ", ".join(puntuaciones)
        self.Peliculas.setItem(3, 0, QtWidgets.QTableWidgetItem(puntuacion_comb))


        extras_list = [str(p.get("duracion", "N/A")) for p in peliculas]
        extras_comb = ", ".join(extras_list)
        self.Peliculas.setItem(4, 0, QtWidgets.QTableWidgetItem(extras_comb))

        self._llenar_poster_container(peliculas)

        self.resize(800, 600)
        self.setMinimumSize(600, 400)
        self.frameposterContainer.setMinimumSize(260, 360)

    def _llenar_poster_container(self, peliculas):

        contenedor = self.frameposterContainer

        old_layout = contenedor.layout()
        if old_layout is not None:
            while old_layout.count():
                item = old_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
            old_layout.deleteLater()
            contenedor.setLayout(None)

        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)
        contenedor.setLayout(layout)

        if len(peliculas) > 1:
            desired_width = 150
        else:
            desired_width = 300

        for peli in peliculas:
            ruta_poster = peli.get("ruta_poster", "")
            lbl = QtWidgets.QLabel()
            lbl.setAlignment(QtCore.Qt.AlignCenter)
            if ruta_poster:
                pixmap = QPixmap(ruta_poster)
                if not pixmap.isNull():
                    pixmap_escalado = pixmap.scaledToWidth(desired_width, QtCore.Qt.SmoothTransformation)
                    lbl.setPixmap(pixmap_escalado)
                    lbl.adjustSize()
                else:
                    lbl.setText("Imagen no disponible")
            else:
                lbl.setText("Sin póster")
            layout.addWidget(lbl)
    def _limpiar_poster_container(self):

        contenedor = self.frameposterContainer
        layout = contenedor.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                w = item.widget()
                if w:
                    w.setParent(None)
            layout.deleteLater()

    def limpiar(self):

        self.Peliculas.clearContents()
        self._limpiar_poster_container()
