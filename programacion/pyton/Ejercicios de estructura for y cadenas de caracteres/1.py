cantidad = int(input("Ingrese la cantidad de números que quiere sumar: "))
suma = 0

for i in range(cantidad):
    numero = float(input("Ingrese un número: "))
    suma += numero

print("La suma de los números ingresados es:", suma)
