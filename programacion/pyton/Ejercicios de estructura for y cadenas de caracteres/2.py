import random

suma = 0
for i in range(20):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    resultado = dado1 + dado2
    suma += resultado
promedio = suma / 20

print("El promedio de la suma de los resultados de 20 tiradas de dos dados es:", promedio)

caras = [0] * 6
for i in range(30):
    cara = random.randint(1, 6)
    caras[cara - 1] += 1

print("Cantidad de veces que salió cada cara en 30 tiradas:")
for i in range(6):
    print("Cara", i+1, ":", caras[i])
