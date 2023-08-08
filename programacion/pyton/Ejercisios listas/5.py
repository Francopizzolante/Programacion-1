def mayorlist():
    mayor=0
    for i in range (len(lista1)):
        if lista1[i]>mayor:
            mayor=lista1[i]
    return mayor
def menorlist():
    menor=lista1[0]
    for i in range (len(lista1)):
        if lista1[i]<menor:
            menor=lista1[i]
    return menor
def promedio():
    promedio=0
    for i in range (len(lista1)):
            promedio=lista1[i]
    return promedio/5

lista1=[]
for i in range (5):
    lista1.append(int(input("ingrese nota")))

print("La nota mas alta es", mayorlist())
print("La nota mas baja es", menorlist())
print("El promedio de notas es", promedio())
