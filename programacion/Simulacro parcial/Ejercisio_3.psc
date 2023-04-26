Algoritmo Ejercisio_3
	totn2<-0
	totn3<-0
	totno<-0
	Escribir "Ingrese un numero o cero para finalizar"
	Leer n
	Mientras n<>0 Hacer
		si n%2 ==0 Entonces
			totn2= totn2+1
		FinSi
		si n%3 ==0 Entonces
			totn3= totn3+1
		SiNo
			totno= totno+1
		FinSi
		
		Leer n
	Fin Mientras
	Escribir "Usted ingreso ", totn2, " divisibles entre 2 ", totn3, " divisibles entre 3 ", "y ", totno " no divisibles entre 3 y 2"
FinAlgoritmo
