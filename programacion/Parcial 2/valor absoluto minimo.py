def valorabsolutominimo(lista):
    v = abs((lista [0]) - (lista [1]))
    for i in range (len(lista)-1):
        x= i+1
        if abs((lista [i]) - (lista [x])) < v:
            v = abs((lista [i]) - (lista [x]))
    return v

lista = [1,10,2,6,10,4,0,5]
print(valorabsolutominimo(lista))