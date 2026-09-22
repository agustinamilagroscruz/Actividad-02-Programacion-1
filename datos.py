"""
Módulo: datos.py
Responsabilidad: Proveer la matriz con los registros iniciales del sistema.
Temática: Reseñas de películas y series.
"""


def obtener_registros():
    """
    Retorna la matriz inicial con los 10 registros de películas y series.
    Estructura de cada registro: [Código (int), Título (str), Género (str), Puntuación (str), Reseña (str)]
    """
    registros = [
        [101, "Horizonte Perdido", "Drama", "4", "Una historia interesante con muy buenas actuaciones y un final emocionante."],
        [102, "El Secreto del Abismo", "Ciencia Ficción", "5", "Excelente película de ciencia ficción con efectos visuales impresionantes y una gran historia."],
        [103, "Risas en la Ciudad", "Comedia", "2", "Una comedia simple con actuaciones regulares y una historia predecible."],
        [104, "Cielo de Medianoche", "Drama", "3", "Un drama profundo con excelente fotografía pero un ritmo algo lento."],
        [105, "La Red Oculta", "Suspenso", "5", "Excelente serie de suspenso que mantiene la tensión en cada episodio con actuaciones impecables."],
        [106, "Crónicas del Tiempo", "Ciencia Ficción", "4", "Una historia fascinante sobre viajes temporales con efectos especiales muy logrados."],
        [107, "Misterio en la Niebla", "Suspenso", "1", "Mala película de suspenso con actuaciones flojas y una historia sin sentido."],
        [108, "Aventura Espacial", "Acción", "3", "Buena película de acción espacial con efectos entretenidos pero personajes poco desarrollados."],
        [109, "Corazón Rebelde", "Drama", "5", "Una obra maestra del drama con una historia conmovedora y actuaciones de primer nivel."],
        [110, "Risas Compartidas", "Comedia", "2", "Una comedia entretenida para pasar el rato aunque no aporta nada nuevo a la historia."]
    ]
    return registros
