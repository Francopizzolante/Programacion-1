b=int(input("Ingrese la base"))
h=int(input("Ingrese altura"))
for i in range(h):
    if i == 0 or i == h - 1:
        print("x" * b)
    else:
        print("x" + " " * (b - 2) + "x")