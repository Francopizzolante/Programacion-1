def crear_archivo(nombre_archivo, cadena):
    with open(nombre_archivo, 'w') as archivo:
        contenido = cadena * 5
        archivo.write(contenido)

def contar_cadena_en_archivo(nombre_archivo, cadena):
    contador = 0

    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        contador = contenido.count(cadena)

    return contador

# Ejemplo de uso
nombre_archivo = "C:\\Users\\franc\\OneDrive\\Escritorio\\programacion\\pyton\\Ejercicios de Archivos\\1\\hola.txt"
cadena = "Hola"

# Crear el archivo con la cadena repetida 5 veces
crear_archivo(nombre_archivo, cadena)

# Contar la cantidad de veces que la cadena aparece en el archivo
resultado = contar_cadena_en_archivo(nombre_archivo, cadena)
print(f"La cadena '{cadena}' aparece {resultado} veces en el archivo.")
