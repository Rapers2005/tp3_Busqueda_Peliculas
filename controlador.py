from PySide6.QtCore import Qt
from resultados_window import ResultadosWindow

class GestorPeliculas:
    def __init__(self, modelo, vista):
        self._modelo = modelo
        self._vista = vista

        self._ventana_resultados = None

        self._vista.pushButton.clicked.connect(self._buscar)
        self._vista.LimpiarBusqueda.clicked.connect(self._limpiar_busqueda)

        self._inicializar_completers()

    def _inicializar_completers(self):

        titulos = self._modelo.obtener_titulos()
        lista_actores = self._obtener_lista_actores()

        self._vista.configurar_completers(titulos, lista_actores)

    def _obtener_lista_actores(self):

        actores_encontrados = set()
        for pelicula in self._modelo.obtener_peliculas():
            for actor_obj in pelicula.actores:
                nombre_actor = actor_obj.nombre if hasattr(actor_obj, 'nombre') else actor_obj
                actores_encontrados.add(nombre_actor)
        return list(actores_encontrados)

    def _buscar(self):

        titulo = self._vista.lineEdit.text().strip()
        actor1 = self._vista.TituloActores.text().strip()
        actor2 = self._vista.TituloActores_2.text().strip()

        if not titulo and not actor1 and not actor2:
            self._vista.mostrar_mensaje("Ingresa un título o actores para buscar.")
            return

        if titulo:
            resultados = self._modelo.buscar_por_titulo(titulo)
            if resultados:
                peliculas_dict = []
                for p in resultados:
                    pd = p.to_dict()
                    pd["ruta_poster"] = self._construir_ruta_poster(p.titulo)
                    peliculas_dict.append(pd)

                if not self._ventana_resultados:
                    self._ventana_resultados = ResultadosWindow()
                self._ventana_resultados.mostrar_resultados(peliculas_dict, busqueda_por_titulo=True)
                self._ventana_resultados.show()
            else:
                self._vista.mostrar_mensaje("No se encontró la película con ese título.")

        else:
            if not actor1 and not actor2:
                self._vista.mostrar_mensaje("Ingresa al menos un actor.")
                return

            resultados = []
            for p in self._modelo.obtener_peliculas():

                if p.actores:
                    nombres_actores = [a.nombre for a in p.actores] if hasattr(p.actores[0], 'nombre') else p.actores
                else:
                    nombres_actores = []


                if actor1 and actor2:
                    if (actor1 in nombres_actores) and (actor2 in nombres_actores):
                        resultados.append(p)
                elif actor1:
                    if actor1 in nombres_actores:
                        resultados.append(p)
                else:
                    if actor2 in nombres_actores:
                        resultados.append(p)

            if resultados:
                peliculas_dict = []
                for p in resultados:
                    pd = p.to_dict()
                    pd["ruta_poster"] = self._construir_ruta_poster(p.titulo)
                    peliculas_dict.append(pd)

                if not self._ventana_resultados:
                    self._ventana_resultados = ResultadosWindow()
                self._ventana_resultados.mostrar_resultados(peliculas_dict, busqueda_por_titulo=False)
                self._ventana_resultados.show()
            else:
                self._vista.mostrar_mensaje("No se encontraron películas comunes para esos actores.")

    def _limpiar_busqueda(self):

        self._vista.limpiar_interfaz()
        if self._ventana_resultados:
            self._ventana_resultados.limpiar()

    def _construir_ruta_poster(self, titulo_pelicula):
        import os
        base = titulo_pelicula.lower().replace(' ', '_')
        extensiones = [".jpg", ".png"]
        for ext in extensiones:
            ruta_imagen = os.path.join("imagenes_posters", base + ext)
            if os.path.exists(ruta_imagen):
                return ruta_imagen
        return os.path.join("imagenes_posters", "no_image_available.jpg")
