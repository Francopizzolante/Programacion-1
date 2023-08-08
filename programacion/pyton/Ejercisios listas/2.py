numeros =[]

n=0
while n>0:
    n = int(input("Ingrese un numero:"))
    if n>0:
        numeros.append(n)

print("numeros pares:")
for i in range (len(numeros)):
    if numeros[i] % 2 == 0:
        print (numeros[i])