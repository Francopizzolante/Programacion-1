Algoritmo MiTienda
	Escribir "Ingrese el peso del producto"
	Leer n
	Escribir "Ingrese la tarifa del producto"
	Leer t
	p<-0
	Si n>5 Entonces
		p<-(n*(t/2))
	SiNo
		Si n>3 Entonces
			t<-t-((t*30)/100)
			p<-t*n
		SiNo
			p<-t*n
		Fin Si
	Fin Si
	Escribir "El precio es " p
	
FinAlgoritmo
