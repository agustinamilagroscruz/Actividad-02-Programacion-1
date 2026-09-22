"""
Módulo: consultas.py
Responsabilidad: Búsquedas, filtros y consultas sobre la matriz de registros.
"""


def buscar_por_codigo(matriz, codigo):
    """
    Realiza una búsqueda secuencial de un registro a partir de su código.
    Retorna el registro si lo encuentra, o None si no existe en la matriz.
    """
    for fila in matriz:
        if fila[0] == codigo:
            return fila
    return None


def buscar_por_palabra(matriz, expresion):
    """
    Busca una palabra o expresión dentro de las reseñas de todos los registros.
    La búsqueda no distingue entre mayúsculas y minúsculas.
    Retorna:
    - matriz_filtrada: nueva matriz con los registros que contienen la expresión.
    - total_apariciones: cantidad total de veces que aparece la expresión en todas las reseñas.
    """
    matriz_filtrada = []
    total_apariciones = 0
    expresion_buscada = expresion.lower()

    for fila in matriz:
        resena_en_minuscula = fila[4].lower()
        if expresion_buscada in resena_en_minuscula:
            matriz_filtrada.append(fila)
            apariciones_en_registro = resena_en_minuscula.count(expresion_buscada)
            total_apariciones = total_apariciones + apariciones_en_registro

    return matriz_filtrada, total_apariciones


def filtrar_por_genero(matriz, genero):
    """
    Genera una nueva matriz con los registros que pertenecen al género indicado.
    """
    matriz_filtrada = []
    genero_buscado = genero.lower()

    for fila in matriz:
        if fila[2].lower() == genero_buscado:
            matriz_filtrada.append(fila)

    return matriz_filtrada


def obtener_generos_disponibles(matriz):
    """
    Retorna una lista con todos los géneros presentes en la matriz sin elementos repetidos.
    """
    generos = []
    for fila in matriz:
        genero = fila[2]
        if genero not in generos:
            generos.append(genero)
    return generos
