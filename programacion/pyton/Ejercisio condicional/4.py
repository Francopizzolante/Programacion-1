def funcion4():
    if n>linf and n<lsup:
        vf = True
    else: 
        vf = False
    if vf:
        print("El número pertenece al intervalo")
    else:
        print("El número no pertenece al intervalo")

n = float(input("Ingrese un número: "))
linf = float(input("Ingrese un límite inferior: "))
lsup = float(input("Ingrese un límite superior: "))
funcion4()