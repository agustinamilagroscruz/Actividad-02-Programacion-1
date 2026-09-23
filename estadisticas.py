"""
Módulo: estadisticas.py
Responsabilidad: Cálculos estadísticos independientes sobre la matriz de registros.
"""


def calcular_total_registros(matriz):
    """
    Calcula y retorna la cantidad total de registros en la matriz.
    """
    return len(matriz)


def calcular_cantidad_por_genero(matriz, genero):
    """
    Calcula y retorna la cantidad de registros que pertenecen a un género determinado.
    """
    contador = 0
    genero_buscado = genero.lower()
    for fila in matriz:
        if fila[2].lower() == genero_buscado:
            contador = contador + 1
    return contador


def calcular_promedio_puntuacion(matriz):
    """
    Calcula el promedio de las puntuaciones de todos los registros.
    Convierte explícitamente la puntuación almacenada como cadena de texto a entero.
    """
    if len(matriz) == 0:
        return 0.0

    suma_puntuaciones = 0
    for fila in matriz:
        puntuacion_numerica = int(fila[3])
        suma_puntuaciones = suma_puntuaciones + puntuacion_numerica

    promedio = suma_puntuaciones / len(matriz)
    return promedio


def calcular_longitud_promedio_resenas(matriz):
    """
    Calcula el promedio de longitud (en caracteres) de las reseñas de la matriz.
    """
    if len(matriz) == 0:
        return 0.0

    suma_longitudes = 0
    for fila in matriz:
        longitud_actual = len(fila[4])
        suma_longitudes = suma_longitudes + longitud_actual

    promedio_longitud = suma_longitudes / len(matriz)
    return promedio_longitud


def obtener_registro_resena_mas_larga(matriz):
    """
    Determina y retorna el registro completo que posee la reseña con mayor cantidad de caracteres.
    Aplica el algoritmo de búsqueda de máximo.
    """
    registro_mayor = -1

    if len(matriz) > 0:
        registro_mayor = matriz[0]
        longitud_maxima = len(registro_mayor[4])

        for fila in matriz:
            longitud_actual = len(fila[4])

            if longitud_actual > longitud_maxima:
                longitud_maxima = longitud_actual
                registro_mayor = fila

    return registro_mayor
