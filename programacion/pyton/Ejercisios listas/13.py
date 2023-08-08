def validar_piezas_dentales(cadena):
    numeros = cadena.split(",")
    for numero in numeros:
        numero = int(numero)
        if not (11 <= numero <= 18) and not (21 <= numero <= 28) and not (31 <= numero <= 38) and not (41 <= numero <= 48) and not (51 <= numero <= 55) and not (61 <= numero <= 65) and not (71 <= numero <= 75) and not (81 <= numero <= 85):
            return False
    return True

cadena =input("Ingrese la cadena de números separados por comas: ")
print (validar_piezas_dentales(cadena))