def funcion11a():
    if h1 < h2:
        vf = True
    elif h1 == h2 and m1 < m2:
        vf = True
    elif h1 == h2 and m1 == m2 and s1 < s2:
        vf = True
    else:
        vf = False    
    print (vf)

h1=int(input("Ingrese la hora"))
m1=int(input("Ingrese los minutos"))
s1=int(input("Ingrese los segundos"))
h2=int(input("Ingrese la hora"))
m2=int(input("Ingrese los minutos"))
s2=int(input("Ingrese los segundos"))
funcion11a()

