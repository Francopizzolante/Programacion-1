def intercalar_archivos(archivo1, archivo2, archivo_destino):
    with open(archivo1, 'r') as file1, open(archivo2, 'r') as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()
        max_lines = max(len(lines1), len(lines2))

    with open(archivo_destino, 'w') as file_destino:
        for i in range(max_lines):
            if i < len(lines1):
                file_destino.write(lines1[i])
            if i < len(lines2):
                file_destino.write(lines2[i])

# Ejemplo de uso
archivo1 = r"C:\Users\franc\OneDrive\Escritorio\programacion\pyton\Ejercicios de Archivos\2\1.txt"
archivo2 = r"C:\Users\franc\OneDrive\Escritorio\programacion\pyton\Ejercicios de Archivos\2\2.txt"
archivo_destino = "archivo_destino.txt"

intercalar_archivos(archivo1, archivo2, archivo_destino)
