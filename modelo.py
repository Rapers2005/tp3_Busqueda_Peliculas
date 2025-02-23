import json
import os


class Pelicula:
    def __init__(self, titulo, actores, sinopsis, puntuacion, anio, duracion):
        self.__titulo = titulo
        self.__actores = actores
        self.__sinopsis = sinopsis
        self.__puntuacion = puntuacion
        self.__anio = anio
        self.__duracion = duracion


    @property
    def titulo(self):
        return self.__titulo


    @property
    def actores(self):
        return self.__actores


    @property
    def sinopsis(self):
        return self.__sinopsis


    @property
    def puntuacion(self):
        return self.__puntuacion

    @puntuacion.setter
    def puntuacion(self, nueva_puntuacion):
        if 0 <= nueva_puntuacion <= 10:
            self.__puntuacion = nueva_puntuacion
        else:
            raise ValueError("La puntuación debe estar entre 0 y 10.")


    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, nuevo_anio):
        if 1800 <= nuevo_anio <= 2100:
            self.__anio = nuevo_anio
        else:
            raise ValueError("El año debe ser válido.")


    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, nueva_duracion):
        if nueva_duracion > 0:
            self.__duracion = nueva_duracion
        else:
            raise ValueError("La duración debe ser un número positivo.")


    def __str__(self):
        return f"{self.titulo} ({self.anio}) - Puntuación: {self.puntuacion}/10, Duración: {self.duracion} min"


    def to_dict(self):
        return {
            "titulo": self.titulo,
            "actores": self.actores,
            "sinopsis": self.sinopsis,
            "puntuacion": self.puntuacion,
            "anio": self.anio,
            "duracion": self.duracion
        }


class PeliculasModel:
    def __init__(self, archivo_json="peliculas.json"):
        self.archivo_json = archivo_json
        self.__peliculas = self.__cargar_peliculas()


    def __cargar_peliculas(self):
        if not os.path.exists(self.archivo_json):
            return []

        with open(self.archivo_json, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return [Pelicula(**pelicula) for pelicula in datos]


    def __guardar_peliculas(self):
        with open(self.archivo_json, "w", encoding="utf-8") as archivo:
            json.dump([pelicula.to_dict() for pelicula in self.__peliculas], archivo, indent=4)


    def obtener_titulos(self):
        return [pelicula.titulo for pelicula in self.__peliculas]


    def obtener_peliculas(self):
        return self.__peliculas


    def buscar_por_titulo(self, titulo):
        return [pelicula for pelicula in self.__peliculas if titulo.lower() in pelicula.titulo.lower()]


    def agregar_pelicula(self, pelicula):
        if any(p.titulo.lower() == pelicula.titulo.lower() for p in self.__peliculas):
            raise ValueError("Ya existe una película con ese título.")
        self.__peliculas.append(pelicula)
        self.__guardar_peliculas()


    def eliminar_pelicula(self, titulo):
        peliculas_filtradas = [p for p in self.__peliculas if p.titulo.lower() != titulo.lower()]
        if len(peliculas_filtradas) == len(self.__peliculas):
            raise ValueError("La película no se encontró en la lista.")
        self.__peliculas = peliculas_filtradas
        self.__guardar_peliculas()


    def actualizar_pelicula(self, titulo, nuevos_datos):
        for pelicula in self.__peliculas:
            if pelicula.titulo.lower() == titulo.lower():
                if 'titulo' in nuevos_datos:
                    pelicula.__titulo = nuevos_datos['titulo']
                if 'actores' in nuevos_datos:
                    pelicula.__actores = nuevos_datos['actores']
                if 'sinopsis' in nuevos_datos:
                    pelicula.__sinopsis = nuevos_datos['sinopsis']
                if 'puntuacion' in nuevos_datos:
                    pelicula.puntuacion = nuevos_datos['puntuacion']
                if 'anio' in nuevos_datos:
                    pelicula.anio = nuevos_datos['anio']
                if 'duracion' in nuevos_datos:
                    pelicula.duracion = nuevos_datos['duracion']
                self.__guardar_peliculas()
                return
        raise ValueError("No se encontró la película para actualizar.")
