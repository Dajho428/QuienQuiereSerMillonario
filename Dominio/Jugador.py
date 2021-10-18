from Dominio import Contacto
from Dominio.Historial import Historial


class Jugador():

    def __init__(self, idJugador, nombre, apellido):
        self.idJugador = idJugador
        self.nombre = nombre
        self.apellido = apellido
        self.dineroGanado = 0
        self.historial = None
        self.contactos = []
