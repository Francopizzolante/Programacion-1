def segundos():
    s= (s+(h*3600)+(m*60))
    print("la hora en segundos es",s)

h=int(input("Ingrese la hora"))
m=int(input("Ingrese los minutos"))
s=int(input("Ingrese los segundos"))

segundos()