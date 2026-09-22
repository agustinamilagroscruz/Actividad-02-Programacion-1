"""
Módulo: validaciones.py
Responsabilidad: Control y validación de las entradas de usuario por teclado (sin try/except).
"""


def solicitar_opcion_menu(minimo=1, maximo=9):
    """
    Solicita al usuario una opción numérica para el menú y valida que sea un entero en el rango especificado.
    No utiliza manejo de excepciones (try/except).
    """
    while True:
        entrada = input(f"\nSeleccione una opción ({minimo}-{maximo}): ").strip()
        if entrada.isdigit():
            opcion = int(entrada)
            if minimo <= opcion <= maximo:
                return opcion
            else:
                print(f"[ERROR] La opción debe estar entre {minimo} y {maximo}.")
        else:
            print("[ERROR] Debe ingresar un número entero válido.")


def solicitar_codigo_entero(mensaje="Ingrese el código del registro: "):
    """
    Solicita un código de registro al usuario y valida que sea un número entero positivo.
    No utiliza manejo de excepciones.
    """
    while True:
        entrada = input(mensaje).strip()
        if entrada.isdigit():
            return int(entrada)
        print("[ERROR] El código debe ser un número entero positivo.")


def solicitar_genero_valido(generos_disponibles):
    """
    Muestra la lista de géneros disponibles numerados y solicita al usuario seleccionar uno válido.
    Retorna el nombre del género seleccionado.
    """
    print("\n--- GÉNEROS DISPONIBLES ---")
    for indice in range(len(generos_disponibles)):
        print(f"{indice + 1}. {generos_disponibles[indice]}")

    cantidad_generos = len(generos_disponibles)
    while True:
        entrada = input(f"\nSeleccione el número de género (1-{cantidad_generos}): ").strip()
        if entrada.isdigit():
            opcion = int(entrada)
            if 1 <= opcion <= cantidad_generos:
                genero_seleccionado = generos_disponibles[opcion - 1]
                return genero_seleccionado
            else:
                print(f"[ERROR] Debe ingresar una opción entre 1 y {cantidad_generos}.")
        else:
            print("[ERROR] Debe ingresar un número entero válido.")


def solicitar_texto_no_vacio(mensaje="Ingrese un texto: "):
    """
    Solicita un texto al usuario y valida que no se encuentre vacío ni contenga solo espacios.
    Retorna el texto ingresado.
    """
    while True:
        entrada = input(mensaje).strip()
        if len(entrada) > 0:
            return entrada
        print("[ERROR] El texto ingresado no puede estar vacío ni contener solo espacios.")


def solicitar_separador(mensaje="Ingrese el nuevo separador (o presione ENTER para usar ' - '): "):
    """
    Solicita un separador para reconstruir cadenas.
    Si el usuario presiona ENTER sin escribir nada, retorna ' - ' por defecto.
    """
    entrada = input(mensaje)
    if len(entrada) == 0:
        return " - "
    return entrada
