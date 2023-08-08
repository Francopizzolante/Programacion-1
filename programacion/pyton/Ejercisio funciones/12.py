def bisiesto():
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        s=True
    else:
        s=False
    print (s)

a=int(input("Ingrese un año"))

bisiesto()