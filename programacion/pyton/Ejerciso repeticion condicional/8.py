def calcular_sumatoria(n):
    resultado = 0
    for k in range(n):
        termino = (1/6)**k * ((4/(8*k+1)) - (2/(8*k+4)) - (1/(8*k+5)) - (1/(8*k+6)))
        resultado += termino
    return resultado
numero = int(input("Ingresa un número: "))
calcular_sumatoria(numero)
print (numero) 
