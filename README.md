# TP3 - Búsqueda de Películas

## Descripción
Este proyecto es una aplicación de búsqueda de películas que permite realizar consultas por título o por actores.Basado en el MVC (modelo-vista-controlador) Utiliza PySide6 para la interfaz gráfica y puede cargar catálogos de películas tanto de una lista predefinida como desde un archivo JSON.
Contempla la accion de "doble click" para limpiar "ingresar titulo", ya sea por primera vez o siguientes, asi como tambien en el cajon de linea de "Actor1" y "Actor2", se puede ingresar con tanto con minusculas como con mayusculas el nombre de titulo de peliculas o de los actores, al ingresar la primer letra ya se despliega una lista con los nombres que comiencen con esa letra, en cualquiera de las búsquedas. En la búsqueda por actores se obtiene la/s películas que filmaron juntos (dos actores) Se cargan las imagenes o psters de una de lista de peliculas almacenadas en lista de diccionarios. En el cajon de busqueda avanzada se puede cargar un archivo Json, con una cantidad mas amplia de peliculas, no contiene imagenes ya que sus URL estan "caidas", se contemplo conectar con una API, para poder obtener online los posters o imagenes siempre y cuando existan en la misma. Se incluye decoradores de funciones.
Para el diseño de la interfaz se utilizo Qtdesigner con su respectiva configuración, desde su código, se genero el codigo python(lenguaje de alto nivel) y desde éste, se desarrollo el proyecto.


## Requisitos #Instalacion
- Python 3.12
- PySide6
- Otras dependencias que puedes instalar con el siguiente comando:
```bash
pip install -r requirements.txt

Instrucciones sobre cómo instalar el proyecto en un entorno local.

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/tu-repositorio.git

# Moverse al directorio del proyecto
cd nombre-del-directorio

# Crear un entorno virtual
python -m venv env

# Activar el entorno virtual
# En Windows
env\Scripts\activate
# En Mac/Linux
source env/bin/activate




