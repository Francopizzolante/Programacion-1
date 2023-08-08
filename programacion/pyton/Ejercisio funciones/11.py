import math

def calc():
     d = ((b**2)-(4*a*c))
     if d < 0:
          print("El polinomio no tiene raíces reales.")
     else:
          r1 = ((-b + math.sqrt(d)) / (2*a))
          r2 = ((-b - math.sqrt(d)) / (2*a))
          print("Las raíces del polinomio son:", r1, "y", r2)

a=int(input("Ingrese a"))
b=int(input("Ingrese b"))
c=int(input("Ingrese c"))

calc()