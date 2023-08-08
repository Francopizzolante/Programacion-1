def duplicados(lista, lista2):
    lista3 = []
    for e in lista:
        if e not in lista3:
            lista3.append(e)
    for e in lista2:
        if e not in lista3:
            lista3.append(e)
    for e in lista:
        if e in lista2:
            while e in lista3:
                lista3.remove(e)
    return lista3

lista = [1, 2, 3, 4, 5, 6, 5]
lista2 = [1, 2, 7, 4, 8, 9]
lista3 = duplicados(lista, lista2)

print(lista3)