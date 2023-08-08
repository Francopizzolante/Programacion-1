def buscar_cadena_en_archivo(archivo_nombre, cadena):
    lineas_coincidentes = []
    
    with open(archivo_nombre, "r", encoding='utf8', errors="ignore") as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            if cadena in linea:
                lineas_coincidentes.append(numero_linea)
    
    return lineas_coincidentes

archivo_nombre = r"C:\Users\franc\OneDrive\Escritorio\programacion\pyton\Ejercicios de Archivos\4\ej4-archivo.txt"
cadena_buscar = "golondrinas"

lineas_encontradas = buscar_cadena_en_archivo(archivo_nombre, cadena_buscar)
print("La cadena se encontró en las siguientes líneas:", lineas_encontradas)