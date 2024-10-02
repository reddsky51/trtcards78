import random

def elegir_numeros_aleatorios(total, cantidad):
    return random.sample(range(1, total + 1), cantidad)
numeros_aleatorios = elegir_numeros_aleatorios(72, 36)
print(numeros_aleatorios)
