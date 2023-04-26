d = int(input("Ingrese el número del día de la semana (1 a 7): "))

if d == 1:
    print("Hoy comienza la semana. Ánimo!")
elif d == 5:
    print("Ya casi termina!")
elif d == 6 or d == 7:
    print("Siiii! Fin de semana!")
elif d >= 2 and d <= 7:
    print("Vamos que se puede!")
else:
    print("El número ingresado no es válido. Por favor ingrese un número entre 1 y 7.")