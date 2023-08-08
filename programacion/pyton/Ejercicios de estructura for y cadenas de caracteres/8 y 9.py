def valor_gematrico(cadena):
    suma = 0
    valores_letras = ["", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in cadena.lower():
        if i in valores_letras:
            suma += valores_letras.index(i)
    return suma
def es_magica(cadena):
    if valor_gematrico(cadena) == 21:
        return True
    else:
        return False
        
cadena = str(input("Ingrese una secuencia"))
print(valor_gematrico(cadena))
print(es_magica(cadena))