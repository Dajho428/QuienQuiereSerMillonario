class Juego():
    def __init__(self, idJuego, jugador, dificultad, categoria, preguntas, respuestas, comodines):
        self.idJuego = idJuego
        self.jugador = jugador
        self.dificultad = dificultad
        self.categoria = categoria
        self.preguntas = preguntas
        self.respuestas = respuestas
        self.comodines = comodines
        self.dineroAcumulado=0
