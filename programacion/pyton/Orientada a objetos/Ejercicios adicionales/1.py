class Auto:
    def __init__(self, marca, color, año):
        self.marca = marca
        self.color = color
        self.año = año
        self.en_movimiento = False
    
    def __str__(self):
        return f"Marca: {self.marca}, Color: {self.color}, Año: {self.año}"
    
    def arrancar(self):
        if self.en_movimiento:
            print("El auto ya está en movimiento")
        else:
            self.en_movimiento = True
            print("El auto ha arrancado")
    
    def frenar(self):
        if self.en_movimiento:
            self.en_movimiento = False
            print("El auto se ha detenido")
        else:
            print("El auto ya está detenido")


mi_auto = Auto("Toyota", "Rojo", 2022)

print(mi_auto)


mi_auto.arrancar()

mi_auto.arrancar()

mi_auto.frenar()

mi_auto.frenar()
