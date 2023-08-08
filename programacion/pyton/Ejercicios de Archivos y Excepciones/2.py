def calcular_promedio_notas(archivo):
    total_notas = 0
    cantidad_alumnos = 0

    with open(archivo, 'r') as f:
        for linea in f:
            try:
                _, nota = linea.strip().split()  # Ignoramos el ID del alumno
                total_notas += float(nota)
                cantidad_alumnos += 1
            except ValueError:
                print(f"Advertencia: Ignorando línea inválida '{linea.strip()}'")

    if cantidad_alumnos > 0:
        promedio = total_notas / cantidad_alumnos
        print(f"El promedio de las notas es: {promedio}")
    else:
        print("No se encontraron notas válidas en el archivo.")


while True:
    try:
        archivo = input("Ingresa el nombre del archivo de texto: ")
        calcular_promedio_notas(archivo)
        break
    except FileNotFoundError:
        print(f"No se encontró el archivo '{archivo}'. Inténtalo nuevamente.")
