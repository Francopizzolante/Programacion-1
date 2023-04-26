def ultimodigito(n):
    return n % 10

def sacarultimodigito(n):
    return n // 10

numero = int(input("Ingresa un número entero positivo mayor que 0: "))
suma = 0

while numero > 0:
    suma += ultimodigito(numero)
    numero = sacarultimodigito(numero)

print("La suma de los dígitos del número es:", suma)