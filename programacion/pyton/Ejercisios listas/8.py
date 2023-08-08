def duplicados(lista):
    lista2 = []
    for e in lista:
        lista2.append(e[0]+" "+e[1])
    return lista2

lista = [["Rocky", "Balboa"], ["Muhammad", "Ali"]]
lista2 = duplicados(lista)
print(lista2)