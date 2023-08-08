def promedio_listas(lista): 
    suma =0
    lista2= []
    for i in range (len(lista)):
        suma =0
        for e in range (len(lista[i])):
            suma += lista[i][e]
            prom = (suma / (len(lista[i])))
        lista2.append(prom)
    print(lista2)

lista=[[1,2],[1,3,4],[4],[1,7,-3,9],[3,4,3,3,3]]
promedio_listas(lista)