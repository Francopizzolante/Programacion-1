numeros = []
suma_negativos = 0
cantidad_positivos = 0
suma_positivos = 0

for i in range(6):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)
    if numero < 0:
        suma_negativos += numero
    elif numero > 0:
        cantidad_positivos += 1
        suma_positivos += numero

if cantidad_positivos > 0:
    promedio_positivos = suma_positivos / cantidad_positivos
else:
    promedio_positivos = 0

print("La sumatoria de los números negativos es:", suma_negativos)
print("El promedio de los números positivos es:", promedio_positivos)
