# TP3 - Búsqueda de Películas

Descripción
Este proyecto es una aplicación de búsqueda de películas que permite realizar consultas por título o por actores, y está basado en el patrón de diseño MVC (Modelo-Vista-Controlador). La interfaz gráfica está construida con PySide6, y el catálogo de películas puede cargarse desde una lista predefinida o un archivo JSON (busqueda avanzada)

Características
Búsqueda por título o por actores: Permite buscar películas por su nombre o por los nombres de dos actores que hayan trabajado juntos.
Autocompletado: Al escribir en los campos de búsqueda, se despliega una lista de sugerencias (insensible a mayúsculas/minúsculas) basadas en los datos disponibles.
Limpieza de campos con doble clic: Al hacer doble clic en el campo "Ingresar título" o en los campos "Actor1" y "Actor2", el texto se limpia automáticamente.
Carga de pósters: Se muestra el póster de la película en la búsqueda por título, utilizando imágenes almacenadas localmente 
Carga de archivos JSON: En el modo de búsqueda avanzada, se pueden cargar catálogos de películas adicionales desde un archivo JSON, creada localmente para probar funcionamiento.
Decoradores de funciones: Se implementan decoradores para mejorar la modularidad y reutilización del código.
Interfaz gráfica diseñada con Qt Designer: La interfaz fue creada usando Qt Designer, y el archivo .ui generado se compila a código Python.
Ventanas:
 Se utiliza una ventana principal (para ingresar el título o los actores) y una segunda ventana (peliculas2.ui) para mostrar los resultados (ficha de la película o películas comunes).
Clase Actor en el Modelo:  
  El modelo maneja los actores como objetos `Actor`, no solo como cadenas, facilitando la extensibilidad (por ejemplo, para más atributos).  
Limpieza de campos:  
  Existe un botón "Limpiar Búsqueda" que borra los campos ingresados por el usuario en la ventana principal.

Requisitos
Python 3.12
PySide6
Instalación de dependencias
Puedes instalar todas las dependencias necesarias ejecutando el siguiente comando:


pip install -r requirements.txt
Instalación y configuración en un entorno local
Clonar el repositorio

git clone https://github.com/tu-usuario/tu-repositorio.git
Moverse al directorio del proyecto

cd nombre-del-directorio
Crear un entorno virtual

python -m venv env
Activar el entorno virtual
En Windows

env\Scripts\activate
En Mac/Linux

source env/bin/activate
Instalar las dependencias

pip install -r requirements.txt
Compilación del archivo .ui
Este proyecto utiliza un archivo .ui generado por Qt Designer para definir la interfaz gráfica. Para convertir este archivo .ui a un archivo Python que puede ser utilizado en el proyecto, sigue estos pasos:

Navegar al directorio donde está el archivo .ui:


cd ruta/del/archivo/ui
Compilar el archivo .ui a Python con el siguiente comando:


pyside6-uic peliculas.ui -o ui_peliculas.py
Esto generará un archivo ui_peliculas.py que puedes importar en tu código como módulo Python.

Ejecución del proyecto
Para ejecutar la aplicación, asegúrate de que el entorno virtual esté activado y usa el siguiente comando:



python main.py
Estructura del Proyecto
main.py: Punto de entrada de la aplicación.
modelo.py: Define la lógica de datos y el modelo de la aplicación.
controlador.py: Define la lógica de control y maneja la interacción entre la vista y el modelo.
vista.py: Define la vista de la aplicación utilizando la clase generada a partir del archivo .ui.
resultados_window.py: nueva ventana
ui_peliculas.py: Código generado a partir del archivo .ui para la interfaz gráfica (no modificar manualmente).
ui_peliculas2.py: codigo generado por la nueva ventana  que proviene del archivo .ui
peliculas.ui: Archivo de diseño de la interfaz gráfica, editable con Qt Designer.
peliculas2.ui: segundo archivo de la nueva ventana generado por Qt designer.
Uso
Buscar por título: Ingresa un título en el campo correspondiente y haz clic en "Buscar". Si la película está en la base de datos, se mostrarán los detalles y el póster.
Buscar por actores: Ingresa los nombres de dos actores en los campos correspondientes y haz clic en "Buscar". La aplicación mostrará las películas en las que ambos actores han trabajado juntos.
Carga de JSON: Usa el botón "Búsqueda avanzada" para cargar un archivo JSON con un catálogo extendido de películas. Este archivo debe tener el formato esperado para ser leído correctamente.
Notas
Asegúrate de tener conexión a internet si quieres utilizar la API de OMDb para obtener los pósters.
La carga de archivos JSON es útil para ampliar el catálogo de películas, aunque algunos enlaces a pósters pueden no estar disponibles.
Para editar la interfaz gráfica, puedes abrir peliculas.ui, y, peliculas2. uien Qt Designer, hacer los cambios y luego compilarlo nuevamente.
Se adjunta archivo JSON y una carpeta con imagenes de posters.


Cambios:

Se reemplazo el campo "puntuacion" por "recaudacion" con la informacion pertinente
