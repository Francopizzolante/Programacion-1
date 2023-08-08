import random

lista = [random.randint(1, 10) for _ in range(10)]
for num in lista:
    print(num,"^2 =", num**2,"///", num, "^3 = ", num**3)