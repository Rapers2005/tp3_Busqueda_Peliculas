
from PySide6.QtCore import QObject, Property, Signal

class PeliculasModel:
    def __init__(self):
        self._peliculas = peliculas = [
    {"titulo": "Inception", "actores": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"], "sinopsis": "Sueños y realidades", "puntuacion": 8.8, "anio": 2010, "duracion": 148},
    {"titulo": "The Matrix", "actores": ["Keanu Reeves", "Laurence Fishburne"], "sinopsis": "Realidad virtual", "puntuacion": 8.7, "anio": 1999, "duracion": 136},
    {"titulo": "Good Will Hunting", "actores": ["Matt Damon", "Robin Williams"], "sinopsis": "La historia de un joven genio en matemáticas", "puntuacion": 8.3, "anio": 1997, "duracion": 126},
    {"titulo": "The Dark Knight", "actores": ["Christian Bale", "Heath Ledger"], "sinopsis": "Batman enfrenta al Joker", "puntuacion": 9.0, "anio": 2008, "duracion": 152},
    {"titulo": "Interstellar", "actores": ["Matthew McConaughey", "Anne Hathaway"], "sinopsis": "Un viaje a través del espacio y el tiempo", "puntuacion": 8.6, "anio": 2014, "duracion": 169},
    {"titulo": "John Wick Chapter 4", "actores": ["Keanu Reeves", "Donnie Yen"], "sinopsis": "John Wick contra un nuevo enemigo poderoso", "puntuacion": 8.2, "anio": 2023, "duracion": 169},
    {"titulo": "Les Misérables", "actores": ["Hugh Jackman", "Russell Crowe"], "sinopsis": "Adaptación musical de la novela de Victor Hugo", "puntuacion": 7.6, "anio": 2012, "duracion": 158},
    {"titulo": "Ocean's Eleven", "actores": ["George Clooney", "Brad Pitt"], "sinopsis": "Un grupo de ladrones planea un gran atraco en Las Vegas", "puntuacion": 7.7, "anio": 2001, "duracion": 116},
    {"titulo": "The Departed", "actores": ["Leonardo DiCaprio", "Matt Damon"], "sinopsis": "Infiltración en el mundo del crimen en Boston", "puntuacion": 8.5, "anio": 2006, "duracion": 151},
    {"titulo": "The Prestige", "actores": ["Christian Bale", "Hugh Jackman"], "sinopsis": "Dos magos rivales y sus secretos", "puntuacion": 8.5, "anio": 2006, "duracion": 130}
]


    def obtener_titulos(self):
        """Devuelve una lista de títulos de las películas."""
        return [pelicula["titulo"] for pelicula in self._peliculas]

    def obtener_peliculas(self):
        """Devuelve la lista completa de películas."""
        return self._peliculas

    def buscar_por_titulo(self, titulo):
        """Busca una película por título y devuelve los resultados."""
        return [pelicula for pelicula in self._peliculas if pelicula["titulo"].lower() == titulo.lower()]
