import random

from Dominio.Pregunta import Pregunta

if __name__ == '__main__':
    pregunta = Pregunta('1')
    preguntas2 = pregunta.crearPreguntas('Facil', 'Entretenimiento')
    cantPreg=10
    aleatorio=random.choice(range(cantPreg))
    cantPreg=cantPreg-1
    preg=str(preguntas2.pop(aleatorio))
    print((preg))

