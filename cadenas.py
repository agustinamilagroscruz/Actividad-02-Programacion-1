"""
Módulo: cadenas.py
Responsabilidad: Procesamiento, transformación, rebanado y reconstrucción de cadenas de texto (UVA 4).
"""


def obtener_vista_previa(texto, cantidad=20):
    """
    Genera una vista previa del texto extrayendo los caracteres iniciales y finales.
    Utiliza longitud, índices positivos y negativos mediante rebanadas (slicing).
    Retorna:
    - texto_completo: el texto recibido.
    - longitud_total: longitud total en caracteres.
    - caracteres_iniciales: subcadena con los primeros 'cantidad' caracteres.
    - caracteres_finales: subcadena con los últimos 'cantidad' caracteres.
    """
    longitud_total = len(texto)
    caracteres_iniciales = texto[:cantidad]
    caracteres_finales = texto[-cantidad:]

    return texto, longitud_total, caracteres_iniciales, caracteres_finales


def normalizar_y_transformar(texto, palabra_buscar, palabra_reemplazo):
    """
    Normaliza el texto eliminando espacios iniciales/finales innecesarios,
    aplica un criterio uniforme de minúsculas y realiza el reemplazo de una palabra o expresión.
    Retorna el texto original y la nueva cadena resultante, preservando el original intacto.
    """

    texto_normalizado = texto.strip()

    texto_normalizado = texto_normalizado.lower()

    palabra_buscada_normalizada = palabra_buscar.lower()

    texto_transformado = texto_normalizado.replace(
        palabra_buscada_normalizada,
        palabra_reemplazo
    )

    return texto, texto_transformado


def separar_y_reconstruir(texto, nuevo_separador=" - "):
    """
    Separa un texto en una lista de palabras individuales y lo reconstruye
    utilizando un nuevo separador provisto por el usuario o por defecto.
    Retorna:
    - palabras: lista de palabras obtenidas con split().
    - cantidad_palabras: cantidad total de palabras.
    - texto_reconstruido: nueva cadena formada con join().
    """
    palabras = texto.strip().split()
    cantidad_palabras = len(palabras)
    texto_reconstruido = nuevo_separador.join(palabras)

    return palabras, cantidad_palabras, texto_reconstruido
