def esta(lista, cadena):
    if cadena in lista:
        return True
    else:
        return False

lista = ["manzana", "banana", "naranja"]
cadena = "banana"

if esta(lista, cadena):
    print("La cadena está en la lista")
else:
    print("La cadena no está en la lista")