numero = 1
suma = 0

while numero != 0:
    numero = int(input("Ingresa un número: "))
    if numero > 0:
        suma += numero

print("La sumatoria de los números positivos ingresados es:", suma)
