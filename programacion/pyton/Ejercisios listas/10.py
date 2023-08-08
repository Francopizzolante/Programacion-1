def traductor():
    palabras = frase.split()
    traduccion = []
    for i in range (len(palabras)):
        for n in range (len(español)):
            if palabras[i] == español[n]:
                traduccion.append(ingles[n])
    return traduccion

español = ["es", "hoy", "viernes"]
ingles = ["is", "today", "friday"]
frase = "hoy es viernes"

print(traductor())