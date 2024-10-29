from PySide6.QtCore import QObject, Slot, Property, Qt
from PySide6.QtWidgets import QMessageBox, QCompleter, QFileDialog, QTableWidgetItem
from PySide6.QtGui import QPixmap
import requests
import json
from modelo import PeliculasModel
from vista import MainWindow
import time



class Controlador(QObject):
    def __init__(self, modelo, vista):
        super().__init__()
        self._modelo = modelo
        self._vista = vista

        self._inicializar_completers()


        self._vista.pushButton.clicked.connect(lambda: self._buscar_por_titulo())
        self._vista.pushButton_2.clicked.connect(lambda: self._buscar_por_actores())
        self._vista.pushButtonCargarJSON.clicked.connect(lambda: self._cargar_peliculas_desde_json())

        self._vista.lineEdit.mouseDoubleClickEvent = self._limpiar_campo_titulo
        self._vista.lineEdit_3.mouseDoubleClickEvent = self._limpiar_campo_actor1
        self._vista.lineEdit_4.mouseDoubleClickEvent = self._limpiar_campo_actor2

    def _inicializar_completers(self):
        titulos_peliculas = self._modelo.titulos
        completer = QCompleter(titulos_peliculas)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self._vista.lineEdit.setCompleter(completer)

        lista_actores = self._modelo.lista_actores
        completer_actor_1 = QCompleter(lista_actores, self._vista)
        completer_actor_2 = QCompleter(lista_actores, self._vista)
        completer_actor_1.setCaseSensitivity(Qt.CaseInsensitive)
        completer_actor_2.setCaseSensitivity(Qt.CaseInsensitive)
        self._vista.lineEdit_3.setCompleter(completer_actor_1)
        self._vista.lineEdit_4.setCompleter(completer_actor_2)

    @Slot()
    def _cargar_peliculas_desde_json(self):
        ruta_json, _ = QFileDialog.getOpenFileName(self._vista, "Abrir archivo JSON", "", "Archivos JSON (*.json)")
        if ruta_json:
            self._modelo.cargar_peliculas_desde_json(ruta_json)
            self._actualizar_completer()

    @Slot()
    def _buscar_por_titulo(self):
        titulo = self._vista.lineEdit.text()
        resultados = self._modelo.buscar_por_titulo(titulo)
        if resultados:
            pelicula = resultados[0]
            self._actualizar_tabla_por_titulo(self._vista.Peliculas, pelicula)
            self.mostrar_poster(pelicula["titulo"], pelicula.get("posterurl"), pelicula.get("poster"))
        else:
            self._mostrar_mensaje("No se encontró la película con ese título.")

    def _limpiar_campo_titulo(self, event):
        self._vista.lineEdit.clear()

    def _limpiar_campo_actor1(self, event):
        self._vista.lineEdit_3.clear()

    def _limpiar_campo_actor2(self, event):
        self._vista.lineEdit_4.clear()

    def _actualizar_completer(self):
        titulos_peliculas = self._modelo.titulos
        completer = QCompleter(titulos_peliculas)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self._vista.lineEdit.setCompleter(completer)

        lista_actores = self._modelo.lista_actores
        completer_actor_1 = QCompleter(lista_actores, self._vista)
        completer_actor_2 = QCompleter(lista_actores, self._vista)
        completer_actor_1.setCaseSensitivity(Qt.CaseInsensitive)
        completer_actor_2.setCaseSensitivity(Qt.CaseInsensitive)
        self._vista.lineEdit_3.setCompleter(completer_actor_1)
        self._vista.lineEdit_4.setCompleter(completer_actor_2)

    def _mostrar_mensaje(self, mensaje):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensaje)
        msg.setWindowTitle("Búsqueda de actores")
        msg.exec()

    @Slot()
    def _buscar_por_actores(self):
        actor1 = self._vista.lineEdit_3.text()
        actor2 = self._vista.lineEdit_4.text()
        resultados = self._modelo.buscar_por_actor(actor1, actor2)

        if resultados:
            self._actualizar_tabla_por_actores(self._vista.PeliculasComunes, resultados)
        else:
            self._mostrar_mensaje("No se encontraron películas comunes para estos actores.")

    def _actualizar_tabla_por_titulo(self, tabla, pelicula):
        tabla.setRowCount(5)
        tabla.setItem(0, 0, QTableWidgetItem(pelicula["titulo"]))
        tabla.setItem(1, 0, QTableWidgetItem(", ".join(pelicula["actores"])))
        tabla.setItem(2, 0, QTableWidgetItem(pelicula["sinopsis"]))
        puntuacion_redondeada = round(pelicula["puntuacion"], 2)
        tabla.setItem(3, 0, QTableWidgetItem(str(puntuacion_redondeada)))
        tabla.setItem(4, 0, QTableWidgetItem(f"{pelicula.get('duracion', 'N/A')} min"))

    def _actualizar_tabla_por_actores(self, tabla, resultados):
        if tabla.rowCount() < 2:
            tabla.setRowCount(2)

        tabla.clearContents()

        titulos_peliculas = ", ".join([pelicula["titulo"] for pelicula in resultados])
        anios_peliculas = ", ".join([str(pelicula.get("anio", "N/A")) for pelicula in resultados])

        tabla.setItem(0, 0, QTableWidgetItem(titulos_peliculas))
        tabla.setItem(1, 0, QTableWidgetItem(anios_peliculas))

    @Slot(str, str, str)
    def mostrar_poster(self, titulo_pelicula, poster_url=None, poster_local=None):
        api_key = self.api_key
        if poster_url:
            pixmap = self._cargar_poster_desde_url(poster_url)
        else:
            omdb_poster_url = self.obtener_poster_desde_omdb(titulo_pelicula, api_key)
            if omdb_poster_url:
                pixmap = self._cargar_poster_desde_url(omdb_poster_url)
            else:
                pixmap = None

        if pixmap and not pixmap.isNull():
            self._vista.labelPoster.setPixmap(pixmap.scaled(self._vista.labelPoster.size(), Qt.KeepAspectRatio))
        else:
            self._vista.labelPoster.setText("Imagen no disponible")

    @Property(str, constant=True)
    def api_key(self):
        return "5278dfb4"

    def _cargar_poster_desde_url(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                image_data = response.content
                pixmap = QPixmap()
                pixmap.loadFromData(image_data)
                return pixmap
            else:
                print(f"Error al descargar la imagen. Código de estado: {response.status_code}")
                return None
        except Exception as e:
            print(f"Excepción al intentar descargar la imagen: {e}")
            return None

    def obtener_poster_desde_omdb(self, titulo_pelicula, api_key):
        url = f"http://www.omdbapi.com/?t={titulo_pelicula}&apikey={api_key}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                datos = response.json()
                return datos.get("Poster", None)
            else:
                print(f"Error al consultar OMDB: código {response.status_code}")
                return None
        except Exception as e:
            print(f"Error al obtener el póster desde OMDB: {e}")
            return None