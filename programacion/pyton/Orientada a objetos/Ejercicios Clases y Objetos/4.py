class Persona:
    def __init__(self, cedula, direccion, nombres, apellidos, telefono):
        self.cedula = cedula
        self.direccion = direccion
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono

class CuentaBancaria:
    def __init__(self, saldo, numero_cuenta, dueño):
        self.saldo = saldo
        self.numero_cuenta = numero_cuenta
        self.dueno = dueño

    def deposito(self, monto):
        self.saldo += monto
        return True

    def extraccion(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        else:
            return False

    def transferencia(self, cuenta_destino, monto):
        if self.extraccion(monto):
            return cuenta_destino.deposito(monto)
        else:
            return False

persona1 = Persona("1023456-4", "Rosevelt y rambla", "Juan", "Pérez", "095456723")
cuenta1 = CuentaBancaria(1000, "12345", persona1)

persona2 = Persona("3263456-7", "Avenida italia", "María", "González", "096874252")
cuenta2 = CuentaBancaria(500, "54321", persona2)

print("Saldo inicial cuenta 1:", cuenta1.saldo)
print("Saldo inicial cuenta 2:", cuenta2.saldo)

cuenta1.deposito(200)
cuenta2.extraccion(100)

print("Saldo cuenta 1 después del depósito:", cuenta1.saldo)
print("Saldo cuenta 2 después de la extracción:", cuenta2.saldo)

cuenta1.transferencia(cuenta2, 300)

print("Saldo cuenta 1 después de la transferencia:", cuenta1.saldo)
print("Saldo cuenta 2 después de la transferencia:", cuenta2.saldo)
