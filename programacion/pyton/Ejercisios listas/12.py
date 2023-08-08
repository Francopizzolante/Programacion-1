Oraciones = []
n=""
caracteres=0
while n!=("::q."):
    n = str(input("Ingrese una oracion"))
    n = n.capitalize()
    if n != "":
        if not n.endswith("."):
            n +="."
    print (n)
    if n!=("::q."):
        caracteres += len(n)
        Oraciones.append(n)

print(Oraciones)
print(caracteres)
print (len(Oraciones))