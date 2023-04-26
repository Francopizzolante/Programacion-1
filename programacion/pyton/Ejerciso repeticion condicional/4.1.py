import random

suma = 0
for i in range(20):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma += dado1 + dado2

promedio = suma / 20
print("El promedio de la suma de los resultados de las 20 tiradas de dos dados es:", promedio)

