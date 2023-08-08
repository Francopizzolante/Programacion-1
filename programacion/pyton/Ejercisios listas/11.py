import random 

def carton():
    disponibles = list(range(1, 100))
    carton = []
    for i in range(3):
        fila = []
        for j in range(5):
            numero = random.choice(disponibles)
            disponibles.remove(numero)
            fila.append(numero)
        carton.append(fila)
    return carton

print(carton())