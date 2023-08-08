def duplicados(lista):
    lista2 = []
    for e in lista:
        if e not in lista2:
            lista2.append(e)
    return lista2

lista = [1, 2, 3, 2, 1, 4, 5, 4, 6, 7, 8]
lista2 = duplicados(lista)
print(lista2)