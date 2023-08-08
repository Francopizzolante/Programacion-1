def digito_verificador(ci):
    ci_str = str(ci)
    if not (100000 <= ci <= 9999999):
        return -1
    ponderaciones = [2, 9, 8, 7, 6, 3, 4]
    suma_productos = 0
    for i in range(len(ci_str)):
        suma_productos += int(ci_str[i]) * (ponderaciones[i])
        print(suma_productos)
    resto = suma_productos % 10
    if resto == 0:
        return 0
    else:
        return 10 - resto
def esValida(ci, dv):
    if dv == -1:
        print("El número de cédula ingresado es inválido.")
    else:
        print("El dígito verificador de la cédula", (ci), "es", (dv))

ci = int(input("Ingrese su cedula"))
dv = digito_verificador(ci)
esValida(ci, dv)