def es_lipograma(cadena):
    cadena = cadena.lower()
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    for letra in alfabeto:
        if letra not in cadena:
            if letra == sin:
                continue
            else:
                return False
        
    return True


cadena = 'El viejo Señor Gómez pedía queso, kiwi y habas, pero le ha tocado un saxofón.'
sin = 'w'
if es_lipograma(cadena):
    print(f'La cadena es un lipograma sin la letra {sin}')
else:
    print(f'La cadena no es un lipograma sin la letra {sin}')
