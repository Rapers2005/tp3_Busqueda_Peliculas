import json

class PeliculasModel:
    def __init__(self):

        self._peliculas = [
            {"titulo": "Inception", "actores": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"], "sinopsis": "Sueños y realidades", "puntuacion": 8.8, "anio": 2010, "duracion": 148},
            {"titulo": "The Matrix", "actores": ["Keanu Reeves", "Laurence Fishburne"], "sinopsis": "Realidad virtual", "puntuacion": 8.7, "anio": 1999, "duracion": 136},
            {"titulo": "John Wick: Chapter 4", "actores": ["Keanu Reeves", "Laurence Fishburne"], "sinopsis": "Accion", "puntuacion": 6.7, "anio": 2023, "duracion": 169},
            {"titulo": "The Dark Knight", "actores": ["Christian Bale", "Michael Caine"], "sinopsis": "Batman enfrenta a su mayor enemigo, el Joker.", "puntuacion": 9.0, "anio": 2008, "duracion": 152},
            {"titulo": "The Prestige", "actores": ["Christian Bale", "Michael Caine"], "sinopsis": "Dos magos rivales intentan superarse entre sí con trucos más elaborados.", "puntuacion": 8.5, "anio": 2006, "duracion": 130},
            {"titulo": "Interstellar", "actores": ["Matthew McConaughey", "Anne Hathaway"], "sinopsis": "Un grupo de astronautas busca un nuevo hogar para la humanidad en el espacio.", "puntuacion": 8.6, "anio": 2014, "duracion": 169},
            {"titulo": "Les Misérables", "actores": ["Hugh Jackman", "Anne Hathaway"], "sinopsis": "Adaptación del clásico musical basado en la novela de Victor Hugo.", "puntuacion": 7.6, "anio": 2012, "duracion": 158},
            {"titulo": "The Departed", "actores": ["Leonardo DiCaprio", "Matt Damon"], "sinopsis": "Un policía infiltrado y un espía criminal intentan descubrirse mutuamente en el departamento de policía de Boston.", "puntuacion": 8.5, "anio": 2006, "duracion": 151},
            {"titulo": "Good Will Hunting", "actores": ["Matt Damon", "Robin Williams"], "sinopsis": "Un joven prodigio de las matemáticas debe encontrar su camino en la vida con la ayuda de un terapeuta.", "puntuacion": 8.3, "anio": 1997, "duracion": 126},
            {"titulo": "Ocean's Eleven", "actores": ["Brad Pitt", "George Clooney"], "sinopsis": "Un equipo de ladrones planea robar tres casinos en una sola noche.", "puntuacion": 7.7, "anio": 2001, "duracion": 116}
        ]


    def obtener_peliculas(self):
        return self._peliculas


    def agregar_pelicula(self, pelicula):
        self._peliculas.append(pelicula)

    def cargar_peliculas_desde_json(self, ruta_json):
        try:
            with open(ruta_json, 'r', encoding='utf-8') as archivo:
                datos_json = json.load(archivo)
                peliculas_json = []
                for pelicula in datos_json:
                    # Adaptar los campos del JSON a los que usa la aplicación
                    nueva_pelicula = {
                        "titulo": pelicula["title"],
                        "actores": pelicula["actors"],
                        "sinopsis": pelicula["storyline"],
                        "puntuacion": sum(pelicula["ratings"]) / len(pelicula["ratings"]),
                        "anio": pelicula["year"]
                    }
                    peliculas_json.append(nueva_pelicula)


                self._peliculas = peliculas_json
        except FileNotFoundError:
            print(f"Archivo {ruta_json} no encontrado.")
        except KeyError as e:
            print(f"Error en la estructura del JSON: campo {e} no encontrado.")

    def buscar_por_titulo(self, titulo):
        return [p for p in self._peliculas if titulo.lower() in p["titulo"].lower()]

    def buscar_por_actor(self, actor1, actor2):

        return [p for p in self._peliculas if actor1.lower() in [a.lower() for a in p["actores"]]
                and actor2.lower() in [a.lower() for a in p["actores"]]]

    def obtener_titulos(self):
        return [pelicula["titulo"] for pelicula in self._peliculas]

    def obtener_lista_actores(self):

        lista_actores = []
        for pelicula in self._peliculas:
            lista_actores.extend(pelicula["actores"])
        return list(set(lista_actores))
