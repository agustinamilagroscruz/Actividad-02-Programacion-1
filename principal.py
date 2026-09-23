"""
Módulo: principal.py
Responsabilidad: Punto de entrada del programa. Inicializa los datos y coordina la ejecución.
"""

from datos import obtener_registros
from menu import ejecutar_menu

matriz_registros = obtener_registros()
ejecutar_menu(matriz_registros)


