class Mascota:
    def __init__(self, especie, nombre, color, veterinaria):
        self.especie = especie
        self.nombre = nombre
        self.color = color
        self.veterinaria = veterinaria

    def __str__(self):
        cadena=(f" especie: {self.especie}\n nombre: {self.nombre}\n color: {self.color}\n veterinaria: {self.veterinaria}" )
        return cadena
    
    def obtener_especie(self):
        return self.especie

    def obtener_nombre(self):
        return self.nombre

    def obtener_color(self):
        return self.color

    def obtener_veterinaria(self):
        return self.veterinaria
    
mascota1 = Mascota("Perro", "Fido", "Marrón", "Clínica Veterinaria ABC")

print(mascota1)
