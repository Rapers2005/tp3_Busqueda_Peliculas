from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox, QCompleter
from PySide6.QtGui import QPixmap
import os
from PySide6.QtCore import Qt


class Controlador:
    def __init__(self, modelo, vista):
        self._modelo = modelo
        self._vista = vista

        self._inicializar_completers()

        self._vista.pushButton.clicked.connect(self._buscar)

        self._vista.lineEdit.mouseDoubleClickEvent = lambda event: self._limpiar_campo(self._vista.lineEdit)
        self._vista.lineEdit_3.mouseDoubleClickEvent = lambda event: self._limpiar_campo(self._vista.lineEdit_3)
        self._vista.lineEdit_4.mouseDoubleClickEvent = lambda event: self._limpiar_campo(self._vista.lineEdit_4)

    def _inicializar_completers(self):
        titulos_peliculas = self._modelo.obtener_titulos()
        completer = QCompleter(titulos_peliculas)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self._vista.lineEdit.setCompleter(completer)

        lista_actores = self._obtener_lista_actores()
        completer_actor_1 = QCompleter(lista_actores, self._vista)
        completer_actor_2 = QCompleter(lista_actores, self._vista)
        completer_actor_1.setCaseSensitivity(Qt.CaseInsensitive)
        completer_actor_2.setCaseSensitivity(Qt.CaseInsensitive)
        self._vista.lineEdit_3.setCompleter(completer_actor_1)
        self._vista.lineEdit_4.setCompleter(completer_actor_2)

    def _limpiar_campo(self, campo):
        campo.clear()

    def _buscar(self):
        titulo = self._vista.lineEdit.text().strip()
        actor1 = self._vista.lineEdit_3.text().strip()
        actor2 = self._vista.lineEdit_4.text().strip()

        if not titulo and not actor1 and not actor2:
            self._mostrar_mensaje("Ingresa al menos un criterio de búsqueda.")
            return

        if titulo:

            if titulo == "":
                self._mostrar_mensaje("La búsqueda por película no puede ser vacía.")
                return
            resultados = self._modelo.buscar_por_titulo(titulo)
            if resultados:
                pelicula = resultados[0]
                self._actualizar_tabla_por_titulo(self._vista.Peliculas, pelicula)
                self._mostrar_poster(pelicula.titulo)
                self._vista.labelTituloActores.setText("")
            else:
                self._mostrar_mensaje("No se encontró la película con ese título.")
                self._vista.labelPoster.clear()
        else:

            if not actor1 and not actor2:
                self._mostrar_mensaje("Para buscar por actores, ingresa al menos un actor.")
                return

            if actor1 and actor2:
                resultados = [pelicula for pelicula in self._modelo.obtener_peliculas()
                              if actor1 in pelicula.actores and actor2 in pelicula.actores]
            elif actor1:
                resultados = [pelicula for pelicula in self._modelo.obtener_peliculas()
                              if actor1 in pelicula.actores]
            else:
                resultados = [pelicula for pelicula in self._modelo.obtener_peliculas()
                              if actor2 in pelicula.actores]

            if resultados:
                titulos = ", ".join([p.titulo for p in resultados])
                self._vista.labelTituloActores.setText(f"Película(s): {titulos}")
                self._actualizar_tabla_por_actores(self._vista.PeliculasComunes, resultados)
            else:
                self._mostrar_mensaje("No se encontraron películas para los actores indicados.")
                self._vista.labelTituloActores.setText("")

    def _mostrar_poster(self, titulo_pelicula):
        ruta_carpeta_imagenes = "imagenes_posters"
        nombre_archivo_base = f"{titulo_pelicula.lower().replace(' ', '_').replace(':', '')}"
        extensiones = [".jpg", ".png"]

        for extension in extensiones:
            ruta_imagen = os.path.join(ruta_carpeta_imagenes, f"{nombre_archivo_base}{extension}")
            if os.path.exists(ruta_imagen):
                pixmap = QPixmap(ruta_imagen)
                break
        else:
            pixmap = QPixmap("imagenes_posters/no_image_available.jpg")

        if pixmap.isNull():
            self._vista.labelPoster.setText("Imagen no disponible")
        else:
            self._vista.labelPoster.setPixmap(pixmap.scaled(self._vista.labelPoster.size(), Qt.KeepAspectRatio))

    def _actualizar_tabla_por_titulo(self, tabla, pelicula):
        tabla.setRowCount(6)
        tabla.setItem(0, 0, QtWidgets.QTableWidgetItem(pelicula.titulo))
        tabla.setItem(1, 0, QtWidgets.QTableWidgetItem(", ".join(pelicula.actores)))
        tabla.setItem(2, 0, QtWidgets.QTableWidgetItem(pelicula.sinopsis))
        tabla.setItem(3, 0, QtWidgets.QTableWidgetItem(str(pelicula.puntuacion)))
        tabla.setItem(4, 0, QtWidgets.QTableWidgetItem(str(pelicula.anio)))
        tabla.setItem(5, 0, QtWidgets.QTableWidgetItem(f"{pelicula.duracion} min"))

    def _actualizar_tabla_por_actores(self, tabla, resultados):
        tabla.clearContents()
        titulos_peliculas = ", ".join([pelicula.titulo for pelicula in resultados])
        anios_peliculas = ", ".join([str(pelicula.anio) for pelicula in resultados])
        tabla.setItem(0, 0, QtWidgets.QTableWidgetItem(titulos_peliculas))
        tabla.setItem(1, 0, QtWidgets.QTableWidgetItem(anios_peliculas))

    def _mostrar_mensaje(self, mensaje):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(mensaje)
        msg.setWindowTitle("Búsqueda")
        msg.exec()

    def _obtener_lista_actores(self):
        lista_actores = []
        for pelicula in self._modelo.obtener_peliculas():
            lista_actores.extend(pelicula.actores)
        return list(set(lista_actores))



    def _actualizar_tabla_por_titulo(self, tabla, pelicula):
        tabla.setRowCount(6)
        tabla.setItem(0, 0, QtWidgets.QTableWidgetItem(pelicula.titulo))
        tabla.setItem(1, 0, QtWidgets.QTableWidgetItem(", ".join(pelicula.actores)))
        tabla.setItem(2, 0, QtWidgets.QTableWidgetItem(pelicula.sinopsis))
        tabla.setItem(3, 0, QtWidgets.QTableWidgetItem(str(pelicula.puntuacion)))
        tabla.setItem(4, 0, QtWidgets.QTableWidgetItem(str(pelicula.anio)))
        tabla.setItem(5, 0, QtWidgets.QTableWidgetItem(f"{pelicula.duracion} min"))


    def _actualizar_tabla_por_actores(self, tabla, resultados):
        tabla.clearContents()
        titulos_peliculas = ", ".join([pelicula.titulo for pelicula in resultados])
        anios_peliculas = ", ".join([str(pelicula.anio) for pelicula in resultados])
        tabla.setItem(0, 0, QtWidgets.QTableWidgetItem(titulos_peliculas))
        tabla.setItem(1, 0, QtWidgets.QTableWidgetItem(anios_peliculas))


    def _mostrar_mensaje(self, mensaje):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(mensaje)
        msg.setWindowTitle("Búsqueda")
        msg.exec()
