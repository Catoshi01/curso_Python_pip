# Importamos la librería random
import random

# Definimos una función para generar una jugada aleatoria
def jugada_aleatoria():
  return random.randint(0, 2)

# Definimos una función para determinar el ganador
def ganador(jugada_jugador, jugada_computadora):
  if jugada_jugador == jugada_computadora:
    return "Empate"
  elif (jugada_jugador == 0 and jugada_computadora == 2) or (jugada_jugador == 1 and jugada_computadora == 0) or (jugada_jugador == 2 and jugada_computadora == 1):
    return "Jugador gana"
  else:
    return "Computadora gana"

# Iniciamos el juego
print("Bienvenido al juego de piedra papel y tijera")

# Solicitamos la jugada del jugador
jugada_jugador = input("¿Qué eliges? (piedra, papel o tijera): ")

# Generamos la jugada de la computadora
jugada_computadora = jugada_aleatoria()

# Determinamos el ganador
ganador = ganador(jugada_jugador, jugada_computadora)

# Imprimimos el resultado
print("La computadora eligió {}. El ganador es {}".format(jugada_computadora, ganador))
