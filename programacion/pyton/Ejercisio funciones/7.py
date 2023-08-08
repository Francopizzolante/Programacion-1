def horas():
    e= (s+(h*3600)+(m*60))
    e2= (s2+(h2*3600)+(m2*60))
    sf=e-e2
    print(sf)

h=int(input("Ingrese la hora"))
m=int(input("Ingrese los minutos"))
s=int(input("Ingrese los segundos"))
h2=int(input("Ingrese la hora2"))
m2=int(input("Ingrese los minutos2"))
s2=int(input("Ingrese los segundos2"))

horas()