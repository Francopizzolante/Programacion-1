def vocales():
    respuesta = ""
    vocales = "AEIOUaeiou"
    for i in palabra:
        if i not in vocales:
            respuesta += i
    return respuesta
palabra=str(input("ingrese una palabra: "))
print (vocales())