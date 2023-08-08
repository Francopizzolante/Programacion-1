def concatenar_archivos(lista_archivos, archivo_salida):
    with open(archivo_salida, 'w') as salida:
        for archivo in lista_archivos:
            with open(archivo, 'r') as archivo_actual:
                salida.write(archivo_actual.read())
                salida.write('\n')

archivos = [r"C:\Users\franc\OneDrive\Escritorio\programacion\pyton\Ejercicios de Archivos\5\ej5-archivo1.txt", 
            r"C:\Users\franc\OneDrive\Escritorio\programacion\pyton\Ejercicios de Archivos\5\ej5-archivo2.txt",
            r"C:\Users\franc\OneDrive\Escritorio\programacion\pyton\Ejercicios de Archivos\5\ej5-archivo3.txt"]
concatenar_archivos(archivos, 'archivo_concatenado.txt')
