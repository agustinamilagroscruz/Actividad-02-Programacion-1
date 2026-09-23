"""
Módulo: menu.py
Responsabilidad: Despliegue del menú interactivo y coordinación de las opciones del sistema.
"""

from presentacion import (
    mostrar_titulo,
    mostrar_separador,
    mostrar_tabla_registros,
    mostrar_registro_completo
)
from validaciones import (
    solicitar_opcion_menu,
    solicitar_codigo_entero,
    solicitar_genero_valido,
    solicitar_texto_no_vacio,
    solicitar_separador
)
from consultas import (
    buscar_por_codigo,
    buscar_por_palabra,
    filtrar_por_genero,
    obtener_generos_disponibles
)
from cadenas import (
    obtener_vista_previa,
    normalizar_y_transformar,
    separar_y_reconstruir
)
from estadisticas import (
    calcular_total_registros,
    calcular_cantidad_por_genero,
    calcular_promedio_puntuacion,
    calcular_longitud_promedio_resenas,
    obtener_registro_resena_mas_larga
)


def mostrar_opciones_menu():
    """
    Imprime las opciones disponibles en el menú principal.
    """
    mostrar_titulo("SISTEMA DE RESEÑAS DE PELÍCULAS Y SERIES")
    print("1. Mostrar todos los registros")
    print("2. Consultar un registro por código")
    print("3. Generar una vista previa del texto")
    print("4. Normalizar y transformar un texto")
    print("5. Consultar registros por palabra o expresión")
    print("6. Separar y reconstruir un texto")
    print("7. Consultar registros por categoría (género)")
    print("8. Procesamiento estadístico")
    print("9. Salir")
    mostrar_separador("-")


def ejecutar_opcion_1(matriz):
    """Opción 1: Mostrar todos los registros en formato tabular."""
    mostrar_tabla_registros(matriz, "LISTADO COMPLETO DE RESEÑAS")


def ejecutar_opcion_2(matriz):
    """Opción 2: Consultar y mostrar todos los datos de un registro por código."""
    mostrar_titulo("CONSULTAR REGISTRO POR CÓDIGO")
    codigo = solicitar_codigo_entero("Ingrese el código del registro a consultar: ")
    registro = buscar_por_codigo(matriz, codigo)

    if registro != -1:
        mostrar_registro_completo(registro)
    else:
        print(f"\n[AVISO] No se encontró ningún registro con el código {codigo}.")


def ejecutar_opcion_3(matriz):
    """Opción 3: Vista previa de la reseña con slicing e índices negativos."""
    mostrar_titulo("VISTA PREVIA DE RESEÑA")
    codigo = solicitar_codigo_entero("Ingrese el código del registro: ")
    registro = buscar_por_codigo(matriz, codigo)

    if registro != -1:
        texto, longitud, inicio, fin = obtener_vista_previa(registro[4], cantidad=20)
        print(f"\nTítulo:               {registro[1]} (Código {registro[0]})")
        print(f"Reseña completa:      \"{texto}\"")
        print(f"Longitud total:       {longitud} caracteres")
        print(f"Primeros 20 carac.:   \"{inicio}\"")
        print(f"Últimos 20 carac.:    \"{fin}\"")
    else:
        print(f"\n[AVISO] No se encontró ningún registro con el código {codigo}.")


def ejecutar_opcion_4(matriz):
    """Opción 4: Normalizar y transformar una reseña sin modificar la matriz original."""
    mostrar_titulo("NORMALIZAR Y TRANSFORMAR TEXTO")
    codigo = solicitar_codigo_entero("Ingrese el código del registro: ")
    registro = buscar_por_codigo(matriz, codigo)

    if registro != -1:
        print(f"\nReseña original seleccionada ({registro[1]}):")
        print(f"\"{registro[4]}\"")

        palabra_buscar = solicitar_texto_no_vacio("\nIngrese la palabra o expresión a reemplazar: ")
        palabra_reemplazo = input("Ingrese el nuevo contenido de reemplazo: ")

        original, transformado = normalizar_y_transformar(registro[4], palabra_buscar, palabra_reemplazo)

        print("\n--- RESULTADO DE LA TRANSFORMACIÓN ---")
        print(f"Texto Original:     \"{original}\"")
        print(f"Texto Transformado: \"{transformado}\"")
        print("\n(Nota: La matriz original conserva el texto original intacto).")
    else:
        print(f"\n[AVISO] No se encontró ningún registro con el código {codigo}.")


def ejecutar_opcion_5(matriz):
    """Opción 5: Buscar registros por palabra o expresión y contabilizar apariciones."""
    mostrar_titulo("BÚSQUEDA POR PALABRA O EXPRESIÓN")
    expresion = solicitar_texto_no_vacio("Ingrese la palabra o expresión a buscar en las reseñas: ")

    matriz_filtrada, total_apariciones = buscar_por_palabra(matriz, expresion)

    if len(matriz_filtrada) > 0:
        mostrar_tabla_registros(matriz_filtrada, f"RESULTADOS DE BÚSQUEDA: '{expresion}'")
        print(f"\nRegistros coincidentes: {len(matriz_filtrada)}")
        print(f"Total de apariciones de '{expresion}' en todas las reseñas: {total_apariciones}")
    else:
        print(f"\n[AVISO] No se encontraron registros cuya reseña contenga la expresión '{expresion}'.")


def ejecutar_opcion_6(matriz):
    """Opción 6: Separar palabras con split() y reconstruir texto con join()."""
    mostrar_titulo("SEPARAR Y RECONSTRUIR TEXTO")
    codigo = solicitar_codigo_entero("Ingrese el código del registro: ")
    registro = buscar_por_codigo(matriz, codigo)

    if registro != -1:
        separador = solicitar_separador("\nIngrese el nuevo separador (o presione ENTER para ' - '): ")
        palabras, cantidad_palabras, texto_reconstruido = separar_y_reconstruir(registro[4], separador)

        print(f"\nReseña original:      \"{registro[4]}\"")
        print(f"Cantidad de palabras: {cantidad_palabras}")
        print(f"Palabras obtenidas:   {palabras}")
        print(f"Texto reconstruido:   \"{texto_reconstruido}\"")
    else:
        print(f"\n[AVISO] No se encontró ningún registro con el código {codigo}.")


def ejecutar_opcion_7(matriz):
    """Opción 7: Consultar registros por categoría (género)."""
    mostrar_titulo("CONSULTAR REGISTROS POR GÉNERO")
    generos_disponibles = obtener_generos_disponibles(matriz)
    genero_seleccionado = solicitar_genero_valido(generos_disponibles)

    matriz_filtrada = filtrar_por_genero(matriz, genero_seleccionado)

    if len(matriz_filtrada) > 0:
        mostrar_tabla_registros(matriz_filtrada, f"RESEÑAS DEL GÉNERO: {genero_seleccionado.upper()}")
    else:
        print(f"\n[AVISO] No existen registros correspondientes al género '{genero_seleccionado}'.")


def ejecutar_opcion_8(matriz):
    """Opción 8: Procesamiento estadístico con funciones independientes."""
    mostrar_titulo("PROCESAMIENTO ESTADÍSTICO")

    # 1. Total de registros
    total_registros = calcular_total_registros(matriz)
    print(f"1. Cantidad total de registros: {total_registros}")

    # 2. Cantidad por género seleccionado
    generos_disponibles = obtener_generos_disponibles(matriz)
    genero_seleccionado = solicitar_genero_valido(generos_disponibles)
    cantidad_genero = calcular_cantidad_por_genero(matriz, genero_seleccionado)
    print(f"\n2. Cantidad de registros del género '{genero_seleccionado}': {cantidad_genero}")

    # 3. Promedio de puntuación (conversión str -> int)
    promedio_puntuacion = calcular_promedio_puntuacion(matriz)
    print(f"3. Promedio general de puntuación: {promedio_puntuacion:.2f} / 5")

    # 4. Longitud promedio de reseñas
    longitud_promedio = calcular_longitud_promedio_resenas(matriz)
    print(f"4. Longitud promedio de las reseñas: {longitud_promedio:.2f} caracteres")

    # 5. Registro con la reseña más larga
    registro_mas_largo = obtener_registro_resena_mas_larga(matriz)
    if registro_mas_largo != -1:
        print(f"5. Reseña de mayor longitud:")
        print(f"   - Título: {registro_mas_largo[1]} (Código {registro_mas_largo[0]})")
        print(f"   - Longitud: {len(registro_mas_largo[4])} caracteres")
        print(f"   - Texto: \"{registro_mas_largo[4]}\"")


def ejecutar_menu(matriz):
    """
    Bucle principal del menú interactivo.
    Recibe la matriz como parámetro para evitar el uso de variables globales.
    """
    seguir = True
    while seguir:
        mostrar_opciones_menu()
        opcion = solicitar_opcion_menu(1, 9)

        if opcion == 1:
            ejecutar_opcion_1(matriz)
        elif opcion == 2:
            ejecutar_opcion_2(matriz)
        elif opcion == 3:
            ejecutar_opcion_3(matriz)
        elif opcion == 4:
            ejecutar_opcion_4(matriz)
        elif opcion == 5:
            ejecutar_opcion_5(matriz)
        elif opcion == 6:
            ejecutar_opcion_6(matriz)
        elif opcion == 7:
            ejecutar_opcion_7(matriz)
        elif opcion == 8:
            ejecutar_opcion_8(matriz)
        elif opcion == 9:
            print("\n¡Gracias por utilizar el Sistema de Reseñas de Películas y Series! Hasta luego.\n")
            seguir = False

        if seguir:
            input("\nPresione ENTER para continuar...")
