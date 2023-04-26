numero = 1
mayor = 0

while numero != 0:
    numero = int(input("Ingresa un número: "))
    if numero > mayor:
        mayor = numero
print("El mayor numero ingresado es:", mayor)
