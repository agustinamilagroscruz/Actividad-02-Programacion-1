"""
Módulo: presentacion.py
Responsabilidad: Salida y formateo visual de datos en consola (tablas, registros y encabezados).
"""


def abreviar_texto(texto, longitud_maxima):
    """
    Si el texto supera la longitud máxima, retorna una versión abreviada utilizando slicing.
    Agrega '...' al final para indicar que fue truncado.
    """
    texto_resultado = texto

    if len(texto) > longitud_maxima:
        texto_resultado = texto[:longitud_maxima - 3] + "..."

    return texto_resultado


def mostrar_separador(caracter="-", longitud=100):
    """
    Muestra una línea separadora en pantalla utilizando repetición de cadenas.
    """
    print(caracter * longitud)


def mostrar_titulo(titulo):
    """
    Muestra un título centrado y enmarcado con separadores.
    """
    print()
    mostrar_separador("=")
    print(f"{titulo:^100}")
    mostrar_separador("=")


def mostrar_tabla_registros(matriz, titulo_tabla="LISTADO DE RESEÑAS"):
    """
    Muestra una matriz de registros en formato tabular alineado y prolijo.
    Si la matriz está vacía, informa al usuario.
    """
    if len(matriz) == 0:
        print("\nNo hay registros para mostrar en la tabla.")
    else:
        mostrar_titulo(titulo_tabla)

        encabezado = f"{'Código':^6} | {'Título':<24} | {'Género':<16} | {'Punt. (1-5)':^11} | {'Reseña':<36}"
        print(encabezado)
        mostrar_separador("-")

        for fila in matriz:
            codigo = fila[0]
            titulo = abreviar_texto(fila[1], 24)
            genero = abreviar_texto(fila[2], 16)
            puntuacion = fila[3]
            resena_corta = abreviar_texto(fila[4], 36)

            fila_formateada = f"{codigo:^6} | {titulo:<24} | {genero:<16} | {puntuacion:^11} | {resena_corta:<36}"
            print(fila_formateada)

        mostrar_separador("-")
        print(f"Total de registros listados: {len(matriz)}")


def mostrar_registro_completo(registro):
    """
    Muestra todos los campos detallados de un único registro, incluyendo la reseña completa.
    """
    print("\n--- DETALLE DEL REGISTRO ---")
    print(f"Código:     {registro[0]}")
    print(f"Título:     {registro[1]}")
    print(f"Género:     {registro[2]}")
    print(f"Puntuación: {registro[3]} / 5")
    print(f"Reseña:     {registro[4]}")
    mostrar_separador("-", 60)
