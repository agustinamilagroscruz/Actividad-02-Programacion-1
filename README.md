# Actividad Obligatoria 02 - Programación 1

## Información Académica
- **Institución:** Universidad Argentina de la Empresa (UADE)
- **Facultad:** Facultad de Ingeniería (FAIN)
- **Departamento:** Tecnología Informática Ciclo Inicial (DEINI)
- **Materia:** Programación 1 (Código 16263) - Online
- **Docente:** Lic. Juan Pablo Nardone
- **Cuatrimestre:** Segundo Cuatrimestre 2026
- **Fecha límite de entrega:** Miércoles 23 de septiembre de 2026

### Integrantes del Grupo
- Bianca Freccia - Legajo: 1206377
- Lara Magalí Fodino - Legajo: 1216143
- Patricio Raber - Legajo: 1234652
- Agustina Cruz - Legajo: 1241748

---

## Temática Seleccionada: 1. Reseñas de películas y series

El sistema permite consultar, filtrar, transformar y analizar reseñas de películas y series utilizando una matriz (lista de listas), donde cada fila representa una obra y las columnas corresponden a sus atributos específicos.

### Estructura de Datos (Columnas de la Matriz)
- **Columna 0 - Código:** Identificador numérico único del registro (número entero, ej: `101`).
- **Columna 1 - Título:** Título de la película o serie (cadena de caracteres, ej: `"Horizonte Perdido"`).
- **Columna 2 - Género:** Categoría temática de la obra (cadena de caracteres, ej: `"Drama"`, `"Ciencia Ficción"`, `"Comedia"`, `"Suspenso"`, `"Acción"`).
- **Columna 3 - Puntuación:** Valoración de la obra almacenada obligatoriamente como texto dentro del rango `"1"` a `"5"` (cadena de caracteres, ej: `"4"`).
- **Columna 4 - Reseña:** Texto descriptivo u opinión sobre la obra (cadena de caracteres).

### Datos Iniciales
El sistema inicia con 10 registros cargados previamente (*hardcodeados*) en la matriz, con variedad de géneros, distintas puntuaciones ("1" a "5"), textos de diferentes longitudes y términos compartidos para probar búsquedas insensibles a mayúsculas/minúsculas y conteo de apariciones.

---

## Funcionalidades del Menú Principal
1. **Mostrar todos los registros:** Imprime un listado tabular alineado con encabezados y anchos fijos de columna, abreviando reseñas extensas mediante rebanado (*slicing*) para conservar la alineación.
2. **Consultar un registro por código:** Realiza una búsqueda secuencial por código y muestra todos los datos del registro en formato detallado.
3. **Generar una vista previa del texto:** Solicita el código de un registro y muestra su reseña completa, longitud total, primeros 20 caracteres (`slicing` positivo) y últimos 20 caracteres (utilizando índices negativos).
4. **Normalizar y transformar un texto:** Limpia espacios en los extremos con `strip()`, aplica formato con mayúscula inicial y reemplaza una palabra o expresión mediante `replace()`, mostrando la comparación entre el original y el transformado (sin mutar la matriz original).
5. **Consultar registros por palabra o expresión:** Realiza una búsqueda *case-insensitive* (`lower()`) en las reseñas, genera una nueva matriz con las coincidencias, la muestra en tabla e informa la cantidad de registros y el total de apariciones encontradas (`count()`).
6. **Separar y reconstruir un texto:** Divide la reseña en una lista de palabras con `split()`, informa la cantidad total de palabras y reconstruye el texto utilizando un separador personalizado mediante `join()`.
7. **Consultar registros por categoría (género):** Lista los géneros disponibles, permite al usuario seleccionar uno, genera una nueva matriz filtrada y la muestra en formato tabular.
8. **Procesamiento estadístico:** Presenta un informe estadístico detallado calculado a través de funciones independientes:
   - Cantidad total de registros almacenados.
   - Cantidad de registros pertenecientes a un género seleccionado.
   - Promedio general de puntuación (con conversión explícita de `str` a entero/numérico).
   - Longitud promedio en caracteres de las reseñas.
   - Identificación del registro con la reseña de mayor longitud.
9. **Salir:** Mensaje de despedida y finalización del programa.

---

## Validaciones Implementadas (Sin Manejo de Excepciones)
Siguiendo las restricciones pedagógicas de la materia, **no se utiliza `try/except` ni `raise`**. Todas las validaciones están resueltas algorítmicamente mediante bucles `while`, cadenas y métodos de UVA 4:
- Control de ingreso de números enteros en el menú (rango 1 al 9) mediante `isdigit()`.
- Verificación de existencia real del código ingresado dentro de la matriz.
- Selección válida de categorías/géneros numerados.
- Control de cadenas no vacías y sin espacios en blanco exclusivos mediante `strip()`.

---

## Modularización y Estructura del Código
El proyecto implementa separación de responsabilidades en 8 módulos independientes, comunicados exclusivamente por parámetros y valores de retorno, sin variables globales:

- **`datos.py`:** Contiene la matriz con los 10 registros iniciales.
- **`presentacion.py`:** Funciones de interfaz de salida: encabezados, formateo de tablas alineadas, abreviación de texto y fichas detalladas.
- **`consultas.py`:** Algoritmos de búsqueda secuencial por código, búsqueda textual insensible a mayúsculas/minúsculas y filtrado por género.
- **`cadenas.py`:** Procesamiento de texto (slicing positivo/negativo, normalización, reemplazo, `split()` y `join()`).
- **`estadisticas.py`:** Funciones de cálculo independientes (conteos, promedios, conversiones y búsqueda de máximo).
- **`validaciones.py`:** Funciones de validación y captura de entradas del usuario por teclado.
- **`menu.py`:** Presentación del menú interactivo y coordinación de las opciones.
- **`principal.py`:** Punto de entrada del programa. Carga los datos y lanza la ejecución.

---

## Instrucciones de Ejecución
1. Abrir una terminal en Visual Studio Code dentro de la carpeta del proyecto:
   `c:\Users\Agust\OneDrive\Desktop\Actividad-02-Programacion-1`
2. Ejecutar el siguiente comando:
   ```bash
   python principal.py
   ```
