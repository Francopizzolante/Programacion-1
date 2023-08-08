def palabras_largas(cadena):
    lista = cadena.split(" ")
    lista2 = []
    for i in range (len(lista)):
        if (len(lista[i]))> 5:
            lista2.append((lista[i]))
    return lista2
cadena =input("Ingrese la cadena: ")
print(palabras_largas(cadena))