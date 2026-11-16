# Proyecto CodeTest — Sistema de Gestión de Entrevistas

Aplicación de consola desarrollada en Python para la gestión y evaluación de postulantes a puestos de desarrollo junior. El proyecto fue diseñado bajo los paradigmas de programación estructurada y modular utilizando únicamente los fundamentos básicos del lenguaje.

## Estructura del Proyecto

El sistema está dividido en tres módulos independientes:

* **`main.py`**: Punto de entrada del programa. Contiene el menú interactivo (`match-case`), las listas paralelas de almacenamiento y la coordinación general del flujo de ejecución.
* **`validaciones.py`**: Módulo encargado de solicitar y validar por teclado todas las entradas del usuario (cantidad de postulantes, nombres y calificaciones) mediante recorridos manuales carácter por carácter.
* **`procesamiento.py`**: Módulo que concentra la lógica de negocio: cálculo de promedios, métricas estadísticas (general, máximo, mínimo y conteo por estado), búsqueda secuencial, ordenamiento burbuja sobre listas paralelas y análisis de cadenas de texto.

## Funcionalidades

1. **Carga de postulantes**: Registro de entre 1 y 15 candidatos con nombre completo, nota de prueba técnica (0 a 10) y nota de entrevista psicotécnica (0 a 10).
2. **Listado general**: Visualización ordenada de todos los postulantes cargados junto con sus notas parciales y promedio.
3. **Estadísticas del proceso**: Cálculo del promedio general de la camada, identificación del mejor y peor promedio, y clasificación por estado:
   * *Contratable*: promedio mayor o igual a 6.
   * *En revisión*: promedio mayor o igual a 4 y menor a 6.
   * *Descartado*: promedio menor a 4.
4. **Ranking de postulantes**: Ordenamiento descendente de mayor a menor promedio implementado con el algoritmo de ordenamiento burbuja sincronizado sobre las listas paralelas.
5. **Búsqueda de postulante**: Búsqueda secuencial por nombre exacto para consultar calificaciones individuales.
6. **Análisis de nombre**: Conteo manual de vocales e inversión de texto de un nombre ingresado por teclado.

## Requisitos y Ejecución

* **Requisitos**: Python 3.10 o superior (necesario para el soporte de la estructura `match-case`). No requiere librerías externas.
* **Ejecución**: Desde una terminal ubicada en la carpeta raíz del proyecto, ejecutar:

```bash
python main.py