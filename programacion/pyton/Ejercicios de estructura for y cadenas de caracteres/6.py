def es_pangrama(cadena):
    cadena = cadena.lower()
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    for letra in alfabeto:
        if letra not in cadena:
            return False
    return True

cadena = 'El viejo Señor Gómez pedía queso, kiwi y habas, pero le ha tocado un saxofón.'
if es_pangrama(cadena):
    print('La cadena es un pangrama')
else:
    print('La cadena no es un pangrama')