def billetes(denominaciones,cantidad):
    a= 0
    i= 0
    string = ""
    while (len(denominaciones)) != (i):
        if (cantidad - denominaciones[i]) >= 0:
            cantidad = (cantidad - denominaciones[i])
            a+=1
        else:
            if a != 0:
                string = str(denominaciones[i])+ " x "+ str(a)
                a = 0
                print (string)
                string = ""
            i+=1

denominaciones = [2000,1000,500,200,100,50,20]
cantidad =int(input("Ingrese la cantidad: "))
billetes(denominaciones,cantidad)