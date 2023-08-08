class Persona:
    def __init__(self, cedula, direccion, nombres, apellidos, telefono):
        self.cedula = cedula
        self.direccion = direccion
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono

    def __str__(self):
        cadena = (f" Cédula: {self.cedula}\n Nombres: {self.nombres}\n Apellidos: {self.apellidos}\n Dirección: {self.direccion}\n Teléfono: {self.telefono}")
        return cadena
    
    def obtener_cedula(self):
        return self.cedula

    def obtener_direccion(self):
        return self.direccion

    def obtener_nombres(self):
        return self.nombres

    def obtener_apellidos(self):
        return self.apellidos

    def obtener_telefono(self):
        return self.telefono

persona1 = Persona("1023456-4", "Rosevelt y rambla", "Juan", "Pérez", "095456723")

print (persona1)