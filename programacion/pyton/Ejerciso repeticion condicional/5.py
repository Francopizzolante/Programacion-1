def funcion5():
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        c += 1
    print (c)
n=int(input("Ingrese un numero"))
c = 0
funcion5()