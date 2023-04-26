import random

cara1 = 0
cara2 = 0
cara3 = 0
cara4 = 0
cara5 = 0
cara6 = 0

for i in range(30):
    resultado = random.randint(1, 6)
    if resultado == 1:
        cara1 += 1
    elif resultado == 2:
        cara2 += 1
    elif resultado == 3:
        cara3 += 1
    elif resultado == 4:
        cara4 += 1
    elif resultado == 5:
        cara5 += 1
    else:
        cara6 += 1

print("Cantidad de veces que salió la cara 1:", cara1)
print("Cantidad de veces que salió la cara 2:", cara2)
print("Cantidad de veces que salió la cara 3:", cara3)
print("Cantidad de veces que salió la cara 4:", cara4)
print("Cantidad de veces que salió la cara 5:", cara5)
print("Cantidad de veces que salió la cara 6:", cara6)
