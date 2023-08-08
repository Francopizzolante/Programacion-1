class Bicicleta:
    def __init__(self, marca, color, tamaño, tipo):
        self.marca = marca
        self.color = color
        self.tamaño = tamaño
        self.tipo = tipo

    def __str__(self):
        cadena=(f" Marca: {self.marca}\n Color: {self.color}\n Tamaño: {self.tamaño}\n Tipo: {self.tipo}" )
        return cadena
    
    def obtener_marca(self):
        return self.marca

    def obtener_color(self):
        return self.color

    def obtener_tamaño(self):
        return self.tamaño

    def obtener_tipo(self):
        return self.tipo
    
bicicleta1 = Bicicleta("Trek", "Rojo", "M", "Montaña")
bicicleta2 = Bicicleta("Gt", "Azul", "L", "Ciudad")
bicicleta3 = Bicicleta("Scoot", "Verde", "S", "Montaña")
bicicleta4 = Bicicleta("Baccio", "Negro", "XL", "Ciudad")
bicicleta5 = Bicicleta("Trek", "Blanco", "M", "Montaña")

print(bicicleta1)
print("--------------------")
print(bicicleta2)
print("--------------------")
print(bicicleta3)
print("--------------------")
print(bicicleta4)
print("--------------------")
print(bicicleta5)
