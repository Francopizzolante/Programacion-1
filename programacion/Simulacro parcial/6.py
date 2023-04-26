t=int(input("Ingrese la temperatura"))
if t<0: 
    print("El clima es muyfrio")
elif t>0 and t<=14:
    print("El clima es frio")
elif t>14 and t<=24:
    print("El clima esta templado")
elif t>24 and t<=30:
    print("El clima esta calido")
elif t>30:
    print("El clima es muy caliente")