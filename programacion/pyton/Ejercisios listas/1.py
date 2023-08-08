def mayorlist(lista1):
    mayor=0
    for i in range (len(lista1)):
        if lista1[i]>mayor:
            mayor=lista1[i]
    menor=lista1[0]
    for i in range (len(lista1)):
        if lista1[i]<menor:
            menor=lista1[i]
    return [mayor, menor]


lista1=[48,54,26,47,65,24,99]
resultados= (mayorlist(lista1))
print ("el mayor es", resultados[0], "el menor es", resultados[1])