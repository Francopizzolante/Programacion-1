class Nota:
    def __init__(self, cedula, nombre, nota):
        self.cedula = cedula
        self.nombre = nombre
        self.nota = nota

    def get_cedula(self):
        return self.cedula

    def get_nombre(self):
        return self.nombre

    def get_nota(self):
        return self.nota

    def set_nota(self, nota):
        self.nota = nota


class Grupo:
    def __init__(self, nombre_grupo, salon):
        self.nombre_grupo = nombre_grupo
        self.salon = salon
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def grabar_resultados(self):
        notas_aprobadas = [nota for nota in self.notas if nota.get_nota() >= 61]
        notas_aprobadas = sorted(notas_aprobadas, key=lambda x: x.get_nota(), reverse=True)
        
        with open("ResultadosP1.txt", "w") as archivo:
            for nota in notas_aprobadas:
                archivo.write(f"{nota.get_nombre()}, {nota.get_nota()}\n")


def cargar_notas(nombre_archivo):
    notas = []
    
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            cedula, nombre, nota = linea.strip().split(",")
            nota = int(nota)
            nueva_nota = Nota(cedula, nombre, nota)
            notas.append(nueva_nota)
    
    return notas

# Crear un objeto Grupo
grupo = Grupo("Grupo 1", "Salón 101")

# Cargar las notas desde un archivo
notas = cargar_notas(r"C:\Users\franc\OneDrive\Escritorio\programacion\pyton\Ejercicios de Archivos\6\ej6-notas.txt")

# Agregar las notas al grupo
for nota in notas:
    grupo.agregar_nota(nota)

# Grabar los resultados de los alumnos aprobados
grupo.grabar_resultados()
