d = {'lunes': 1, 'martes': 2, 'miércoles': 3, 'jueves': 4, 'viernes': 5, 'sábado': 6, 'domingo': 7}
d_l = input("Ingrese el día de la semana: ")

if d_l in d:
    d_n = d[d_l]
else:
    print("El día ingresado no es válido")
    d_n = None
if d_n == 1:
    print("Hoy comienza la semana. Ánimo!")
elif d_n == 5:
    print("Ya casi termina!")
elif d_n == 6 or d_n == 7:
    print("Siiii! Fin de semana!")
elif d_n is not None:
    print("Vamos que se puede!")