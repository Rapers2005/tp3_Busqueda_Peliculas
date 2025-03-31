from resultados_window import ResultadosWindow


class GestorPeliculas:
    def __init__(self, modelo, vista):

        self._modelo = modelo
        self._vista = vista
        self._ventana_resultados = None

        self._vista.buscar_pelicula_signal.connect(self._buscar_por_titulo)
        self._vista.buscar_actores_signal.connect(self._buscar_por_actores)
        self._vista.LimpiarBusqueda.clicked.connect(self._limpiar_busqueda)

        self._inicializar_completers()

    def _inicializar_completers(self):
        titulos = self._modelo.obtener_titulos()
        lista_actores = self._obtener_lista_actores()
        if hasattr(self._vista, 'configurar_completers'):
            self._vista.configurar_completers(titulos, lista_actores)

    def _obtener_lista_actores(self):
        actores_encontrados = set()
        for pelicula in self._modelo.obtener_peliculas():
            for actor_obj in pelicula.actores:
                nombre_actor = actor_obj.nombre if hasattr(actor_obj, 'nombre') else actor_obj
                actores_encontrados.add(nombre_actor)
        return list(actores_encontrados)

    def _buscar_por_titulo(self, titulo):
        if not titulo:
            self._vista.mostrar_mensaje("Ingresa un título para buscar.")
            return
        resultados = self._modelo.buscar_por_titulo(titulo)
        self._mostrar_resultados(resultados, "titulo")

    def _buscar_por_actores(self, actor1, actor2):
        if not actor1 and not actor2:
            self._vista.mostrar_mensaje("Ingresa al menos un actor para buscar.")
            return
        resultados = self._buscar_por_actores_interna(actor1, actor2)
        self._mostrar_resultados(resultados, "actores")

    def _buscar_por_actores_interna(self, actor1, actor2):
        resultados = []
        for p in self._modelo.obtener_peliculas():
            if p.actores:
                if hasattr(p.actores[0], 'nombre'):
                    nombres_actores = [a.nombre for a in p.actores]
                else:
                    nombres_actores = p.actores
            else:
                nombres_actores = []
            if actor1 and actor2:
                if actor1 in nombres_actores and actor2 in nombres_actores:
                    resultados.append(p)
            elif actor1:
                if actor1 in nombres_actores:
                    resultados.append(p)
            else:  # actor2
                if actor2 in nombres_actores:
                    resultados.append(p)
        return resultados

    def _mostrar_resultados(self, resultados, tipo_busqueda):
        if resultados:
            peliculas_dict = []
            for p in resultados:
                pd = p.to_dict()
                pd["ruta_poster"] = self._construir_ruta_poster(p.titulo)
                peliculas_dict.append(pd)
            if not self._ventana_resultados:
                self._ventana_resultados = ResultadosWindow()
            self._ventana_resultados.mostrar_resultados(peliculas_dict, busqueda_por=tipo_busqueda)
            self._ventana_resultados.show()
        else:
            self._vista.mostrar_mensaje("No se encontraron resultados.")

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
