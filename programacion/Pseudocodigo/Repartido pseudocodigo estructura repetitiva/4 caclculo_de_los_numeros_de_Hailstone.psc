Algoritmo caclculo_de_los_numeros_de_Hailstone
	Leer n
	m<-n
	c<-0
	r<-0
	Mientras n<>1 Hacer
		m<-n
		Mientras m>c Hacer
			c<-c+2
		Fin Mientras
		Si c=n Entonces
			n<-n/2
			Escribir n
			c<-0
			r<-r+1
		SiNo
			n<-(n*3)+1
			Escribir n
			c<-0
			r<-r+1
		Fin Si
	Fin Mientras
	Escribir "El resultado es " r
FinAlgoritmo
