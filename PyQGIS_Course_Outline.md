# Curso "Introducción al desarrollo con  PyQGIS"
## Descripción

El curso de "Introducción al desarrollo con PyQGIS" busca dar a conocer a los estudiantes los diferentes escenarios en los cuales es posible utilizar Python en QGIS, con el fin de automatizar flujos de trabajo. Se busca que los estudiantes obtengan un panorama completo de las diferentes opciones por las que pueden optar, según el caso de uso, para optimizar su trabajo con información geográfica.

## Dirigido a

Geógrafos, ingenieros y otros profesionales relacionados con los Sistemas de Información Geográfica y con conocimientos básicos de programación.

## Instructor

Germán Carrillo

[Colaborador oficial de QGIS.](https://github.com/qgis/QGIS/blob/master/doc/CONTRIBUTORS) 

Ingeniero Catastral y Geodesta y Especialista en SIG de la Universidad Distrital Francisco José de Caldas. Máster en Geoinformática de la Universidad de Münster (Alemania). Administrador de GeoTux - Soluciones Geoinformáticas Libres. 

## Sesiones

1) Introducción, consola de Python y editor de scripts.

* Python (1.5h)
* PyQGIS (1.5h)

2) Macros del proyecto. Acciones. (1.5h)

3) Expresiones personalizadas en Python y algoritmos de Geoprocesamiento. (3h)

4) Plugins.  (6h)

5) Scripts 'standalone' (sin la GUI de QGIS). (2.5h)

## Contenido


### 1.a. Introducción

* ¿Para qué programar? 
* Sobre cometer errores en programación.
* ¿Cómo resolver un problema? Partirlo en subtareas.


### 1.b. Python

* Introducción.
* Intérprete de Python.
* Tipos de datos: bool, int, str, list, dict.
* Condicionales y ciclos.
* Funciones.
* Ejercicio: Escribir una función para el cálculo de distancia euclidiana en 2d. La función debe recibir los parámetros X1, Y1, X2, Y2.

### 1.c. Python en QGIS

* Diagrama de introducción.
* Recursos y documentación.
* Escenarios.
* Uso de la consola de Python y el editor de scripts en QGIS
	* Clases y objetos.
	
	* iface.mapCanvas()
	
	* Propiedades de las capas, crear campos.
	
	* Análisis espacial.
	
	* Modificación de capas.
	


### 2.a. Macros del proyecto

* ¿Qué son las macros?
* OpenProject()
	* Abrir consola de Python.
	* Cargar una capa con datos de hoy de x fenómeno/variable.
	* Nombre de capas con fechas.
* SaveProject()
* CloseProject()
  * Apagar capas muy pesadas
* Startup.py (¿Y si lo quiero para cada proyecto en mi máquna?)
	* Abrir consola de Python
	* iface.activeLayer() → variable "l"


### 2.b. Acciones

* ¿Qué son las acciones?
* Ejemplo 1: Abriendo URL de cada aeropuerto
* Ejemplo 2: Seleccionando features con el mismo valor en X campo.


### 3.a. Expresiones personalizadas

* Qué son las expresiones.
* Ejemplo básico expresión personalizada (suma).
* Ejemplo get_elevation().
	* Para seleccionar aeropuerto.
	* Para calcular altura. 
	* Capa de puntos nueva con valor elevación predeterminado.
	* raster_value()!!!
* Ejemplo de generación de QR.


### 3.b. Algoritmos de geoprocesamiento

* Generalidades.
* Recursos.
* Widgets.
* Scripts con decoradores.
* Algoritmo rename field. (actualiza capa).
* Demo: Algoritmo que crea nueva capa (copy vector layer).
* Demo: Model.
* Demo: Algoritmo join espacial que escribe en campo (de la capa aeropuertos) un atributo de la capa departamentos (actualiza capa).

### 4. Plugins

* Programación Orientada a Objetos
* * Ejemplo Clases Geometría y Punto
* PyQt5.
	* Documentación.
	* Módulos: Core, GUI, Widgets.
	* Qt-Designer
		* Controles (Widgets).
		* Layouts.
		* QGIS Custom Widgets.
	* SIGNAL-SLOT.
* Plugins.
	* Copialina (Cheat Sheet).
	* Estructura de plugins para QGIS. (Diagrama)
	* What are some functions of plugins for ([GIS.SE](https://gis.stackexchange.com/questions/131535/what-is-the-purpose-of-some-functions-and-files-in-qgis-python-plugins/132604#132604))
		* Uso del [test plugin](https://github.com/gacarrillor/test/tree/function_notifications_v3).
	* Plugins para desarrolladores: 
		* Plugin reloader.
		* First aid.
		* Plugin builder (opcional)
	* Minimal plugin.
	* Plugin "Hola mundo" con diálogo y botón. (Este puede incluir toolbar personalizada)
	* Plugin con QGIS Custom Widgets: elegir capa para ver resumen.
	* DEMO: Plugin para join espacial Aeropuerto-Departamento.

### 5. Scripts standalone

* Casos de uso.
* iface no disponible.
* Configuración.
	* Windows: OSGeo4W
	* GNU/Linux
* Correr script para imprimir datos de capas.
* Correr script de processing. 
	* Nuevo [qgis-process](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/140)
* Escenarios avanzados en donde se puede usar PyQGIS: 
	* Plugins de QGIS Server.
	* Aplicaciones standalone.
* Otros enlaces de interés.

## Certificado de aprobación

Para acceder a un certificado de aprobación del curso, los estudiantes deberán entregar los ejercicios planteados por el instructor. 
Los estudiantes que cumplan el requisito planteado obtendrán el certificado oficial del proyecto QGIS (en inglés) y opcionalmente obtendrán un certificado de aprobación del curso, expedido por QGIS Colombia (en español).
