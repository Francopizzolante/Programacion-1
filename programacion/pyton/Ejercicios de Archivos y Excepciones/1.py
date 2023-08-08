def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

while True:
    try:
        celsius = float(input("Ingresa la temperatura en grados Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print("La temperatura en grados Fahrenheit es:", fahrenheit)
        break
    except ValueError:
        print("Error: Debes ingresar un valor numérico. Intenta nuevamente.")

