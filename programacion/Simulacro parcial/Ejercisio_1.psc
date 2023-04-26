Algoritmo Ejercisio_1
	Escribir "Ingrese un numero"
	Leer n
	c<-0
	p<-n
	mayor<-n
	menor<-n
	Mientras n<>0 Hacer
		Si n>mayor Entonces
			n=mayor
		Fin Si
		Si n<menor Entonces
			n=menor
		Fin Si
		Escribir "Ingrese un numero"
		Leer n
		c<-c+1
		p<-p+n
		
	Fin Mientras
	p<-p/c
	Escribir "la cantidad de numeros ingresados es ", c
	Escribir "El promedio de los numeros es ", p
	Escribir "el numero mayor es", mayor
	Escribir "el numero menor es", menor
	
FinAlgoritmo
