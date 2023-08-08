class Personaje:
    def __init__(self, nombre, salud, poder, medida_de_daño):
        self.nombre = nombre
        self.salud = salud
        self.poder = poder
        self.medida_de_daño = medida_de_daño
    
    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salud: {self.salud}%")
        print(f"Poder: {self.poder}")
        print(f"Medida de daño: {self.medida_de_daño}")
    
    def atacar(self, otro_personaje):
        otro_personaje.salud -= self.medida_de_daño
    
    def esta_con_vida(self):
        return self.salud > 0


pj1 = Personaje("pj1", 100, "patada giratoria", 50)
pj2 = Personaje("pj2", 80, "golpe de puño", 30)
pj3 = Personaje("pj3", 90, "disparo de fuego", 40)

print("Información de pj1:")
pj1.imprimir_informacion()
print("------------------------------")
print("Información de pj2:")
pj2.imprimir_informacion()
print("------------------------------")
print("Información de pj3:")
pj3.imprimir_informacion()
print("------------------------------")


print("pj1 ataca a pj2")
pj1.atacar(pj2)
pj2.imprimir_informacion()
print("------------------------------")


print ("pj1 ataca a pj3")
pj1.atacar(pj3)
pj3.imprimir_informacion()
print("------------------------------")