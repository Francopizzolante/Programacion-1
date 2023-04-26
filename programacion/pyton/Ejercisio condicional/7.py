def funcion7():
    if (a % 4 == 0) and ((a % 100 != 0) or (a % 400 == 0)):
        vf=True
    else:
        vf=False
    print (vf)

a=int(input("Ingrese un año"))
funcion7()
