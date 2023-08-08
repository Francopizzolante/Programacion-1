import csv

def procesar_informacion(archivo_entrada, opciones):
    # Cargar datos desde el archivo CSV de entrada
    datos = []
    with open(archivo_entrada, 'r') as file:
        reader = csv.reader(file)
        datos = list(reader)

    # Variables predeterminadas
    separador = ","
    columnas = None
    valor_nuevo = None
    nombre_archivo_salida = "clientes_procesados.csv"

    # Aplicar las opciones de procesamiento
    for opcion in opciones:
        if opcion.startswith('-s='):
            separador = opcion.split('=')[1]
            datos = separar_datos(datos, separador)
        elif opcion.startswith('-c='):
            columnas = opcion.split('=')[1].split(',')
            datos = filtrar_columnas(datos, columnas)
        elif opcion.startswith('-a='):
            valor_nuevo = opcion.split('=')[1]
            datos = agregar_columna(datos, valor_nuevo)
        elif opcion.startswith('-o='):
            nombre_archivo_salida = opcion.split('=')[1]

    # Guardar los datos procesados en el archivo de salida
    with open(nombre_archivo_salida, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(datos)

def separar_datos(datos, separador):
    nuevos_datos = []
    for fila in datos:
        fila_separada = [valor.strip() for valor in fila[0].split(separador)]
        nuevos_datos.append(fila_separada)
    return nuevos_datos

def filtrar_columnas(datos, columnas):
    nuevos_datos = []
    for fila in datos:
        fila_filtrada = [fila[int(col)] for col in columnas if int(col) < len(fila)]
        nuevos_datos.append(fila_filtrada)
    return nuevos_datos

def agregar_columna(datos, valor):
    nuevos_datos = []
    for fila in datos:
        fila.append(valor)
        nuevos_datos.append(fila)
    return nuevos_datos

# Solicitar al usuario la entrada de datos
archivo_entrada = (r"c:\Users\franc\OneDrive\Escritorio\programacion\pyton\Ejercicios de Archivos\7\ej7-clientes.csv")
opciones = input("Ingrese las opciones de procesamiento (separadas por espacios): ").split()

# Procesar la información
procesar_informacion(archivo_entrada, opciones)

print("Procesamiento completado.")