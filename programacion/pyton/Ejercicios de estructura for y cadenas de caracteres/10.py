def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

palabra = str(input("escribi una palabra"))
print("¿La palabra", palabra, "es un palíndromo?:", es_palindromo(palabra))