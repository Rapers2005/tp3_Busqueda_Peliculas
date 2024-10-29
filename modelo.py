import json
from PySide6.QtCore import QObject, Property, Signal

class PeliculasModel(QObject):
    peliculasChanged = Signal()

    def __init__(self):
        super().__init__()
        self._peliculas = [
            {"titulo": "Inception", "actores": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"], "sinopsis": "Sueños y realidades", "puntuacion": 8.8, "anio": 2010, "duracion": 148},
            {"titulo": "The Matrix", "actores": ["Keanu Reeves", "Laurence Fishburne"], "sinopsis": "Realidad virtual", "puntuacion": 8.7, "anio": 1999, "duracion": 136},
            # ... (resto de las películas)
        ]

    @Property(list, notify=peliculasChanged)
    def peliculas(self):
        return self._peliculas

    @peliculas.setter
    def peliculas(self, value):
        if self._peliculas != value:
            self._peliculas = value
            self.peliculasChanged.emit()

    def obtener_peliculas(self):
        return self._peliculas

    def agregar_pelicula(self, pelicula):
        self._peliculas.append(pelicula)
        self.peliculasChanged.emit()

    def cargar_peliculas_desde_json(self, ruta_json):
        try:
            with open(ruta_json, 'r', encoding='utf-8') as archivo:
                datos_json = json.load(archivo)
                peliculas_json = []
                for pelicula in datos_json:
                    nueva_pelicula = {
                        "titulo": pelicula["title"],
                        "actores": pelicula["actors"],
                        "sinopsis": pelicula["storyline"],
                        "puntuacion": sum(pelicula["ratings"]) / len(pelicula["ratings"]),
                        "anio": pelicula["year"]
                    }
                    peliculas_json.append(nueva_pelicula)

                self.peliculas = peliculas_json
        except FileNotFoundError:
            print(f"Archivo {ruta_json} no encontrado.")
        except KeyError as e:
            print(f"Error en la estructura del JSON: campo {e} no encontrado.")

    def buscar_por_titulo(self, titulo):
        return [p for p in self._peliculas if titulo.lower() in p["titulo"].lower()]

    def buscar_por_actor(self, actor1, actor2):
        return [p for p in self._peliculas if actor1.lower() in [a.lower() for a in p["actores"]]
                and actor2.lower() in [a.lower() for a in p["actores"]]]

    @Property(list)
    def titulos(self):
        return [pelicula["titulo"] for pelicula in self._peliculas]

    @Property(list)
    def lista_actores(self):
        lista_actores = []
        for pelicula in self._peliculas:
            lista_actores.extend(pelicula["actores"])
        return list(set(lista_actores))