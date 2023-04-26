def funcion10():
    if (a % 4 == 0) and ((a % 100 != 0) or (a % 400 == 0)):
        b=True
    else:
        b=False

    if a <= 0:
        vf = False
    if m < 1 or m > 12:
        vf = False
    if m == 2:
        if b == True:
            if d < 1 or d > 29:
                vf = False
        else:
            if d < 1 or d > 28:
                vf = False
    if m in [4, 6, 9, 11]:
        if d < 1 or d > 30:
            vf = False
    if m in [1, 3, 5, 7, 8, 10, 12]:
        if d < 1 or d > 31:
            vf = False
    print(vf)

a=int(input("Ingrese un año"))
m=int(input("Ingrese un m"))
d=int(input("Ingrese un d"))
funcion10()