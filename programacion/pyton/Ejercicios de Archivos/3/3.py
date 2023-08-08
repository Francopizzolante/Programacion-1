def ingresar_texto():
    texto = ""
    while True:
        linea = input("Ingrese texto ('::q' para finalizar): ")
        if linea == "::q":
            break
        texto += linea + "\n"

    archivo = input("Ingrese el nombre del archivo para guardar el texto: ")
    with open(archivo, 'w') as file:
        file.write(texto)
    print("Texto guardado en el archivo.")

    ver_contenido = input("¿Desea ver el contenido del archivo? (s/n): ")
    if ver_contenido.lower() == "s":
        with open(archivo, 'r') as file:
            contenido = file.read()
            print("Contenido del archivo:")
            print(contenido)

# Ejemplo de uso
ingresar_texto()
