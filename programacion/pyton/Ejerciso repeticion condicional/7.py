def suma_digitos(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma

numero = int(input("Ingresa un número: "))

if suma_digitos(numero) == 21:
    print("El número es de buena suerte!")
else:
    print("El número no es de buena suerte.")
