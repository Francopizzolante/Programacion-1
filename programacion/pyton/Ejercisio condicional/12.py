s = float(input("Ingrese el sueldo acordado: "))
a = int(input("Ingrese la antigüedad (en años): "))
if a >= 20:
    s_a = (s * 0.2)
else:
    s_a = (s * (a / 100))
sr = s*0,11
sm = s* 0,06
if s > 120000:
        ig = s * 0.25
elif s > 70000:
    ig = s * 0.2
else:
    ig = 0
if s > 70000:
      s== (s + s_a) - (ig + sr + sm)
else: 
     s== (s + s_a) - (sr + sm)
print("El sueldo final del trabajador es: $", s)