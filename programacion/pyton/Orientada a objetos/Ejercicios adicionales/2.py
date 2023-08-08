class Auto:
    def __init__(self, marca, color, año, capacidad_tanque, rendimiento):
        self.marca = marca
        self.color = color
        self.año = año
        self.capacidad_tanque = capacidad_tanque
        self.rendimiento = rendimiento
        self.nivel_combustible = 0
        self.kilometraje = 0
    
    def __str__(self):
        return f"Marca: {self.marca}, Color: {self.color}, Año: {self.año}"
    
    def arrancar(self):
        if self.nivel_combustible > 0:
            print("El auto ha arrancado")
        else:
            print("El tanque de nafta está vacío. Cargar nafta para poder arrancar.")
    
    def frenar(self):
        if self.nivel_combustible > 0:
            print("El auto se ha detenido")
        else:
            print("El auto ya está detenido")
    
    def recorrer(self, kms):
        nafta_necesaria = kms / self.rendimiento
        if self.nivel_combustible >= nafta_necesaria:
            self.nivel_combustible -= nafta_necesaria
            self.kilometraje += kms
            print(f"El auto ha recorrido {kms} km")
        else:
            max_kms_posibles = self.nivel_combustible * self.rendimiento
            print(f"No hay suficiente combustible para recorrer {kms} km. "
                  f"Se puede recorrer un máximo de {max_kms_posibles} km.")
    
    def cargar_nafta(self, litros):
        espacio_disponible = self.capacidad_tanque - self.nivel_combustible
        if litros <= espacio_disponible:
            self.nivel_combustible += litros
            print(f"Se han cargado {litros} litros de nafta al tanque.")
        else:
            self.nivel_combustible = self.capacidad_tanque
            exceso_litros = litros - espacio_disponible
            print(f"Se ha llenado el tanque. Sobraron {exceso_litros} litros de nafta.")

mi_auto = Auto("Toyota", "Rojo", 2022, 50, 10)

print(mi_auto)

mi_auto.arrancar()

mi_auto.cargar_nafta(30)

mi_auto.arrancar()

mi_auto.recorrer(200)

mi_auto.frenar()

mi_auto.recorrer(500)

mi_auto.cargar_nafta(20)

mi_auto.recorrer(500)
