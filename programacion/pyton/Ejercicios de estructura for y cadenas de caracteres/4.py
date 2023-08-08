def reemplazar_espacios(cadena):
    nueva_cadena = cadena.replace(' ', ';')
    return nueva_cadena

cadena =str(input("Ingrese una frase"))
print(reemplazar_espacios(cadena))
