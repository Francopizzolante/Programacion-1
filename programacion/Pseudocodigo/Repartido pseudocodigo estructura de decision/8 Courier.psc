Algoritmo Courier
	Escribir "Ingrese el peso del producto en kg"
	Leer n
	p<-0
	Si n<0.9 Entonces
		p<-(n*19.80)
		Escribir "El precio es " p
	SiNo
		Si n<5 Entonces
			p<-(n*21.9)
			Escribir "El precio es " p
		SiNo
			Si n<20 Entonces
				p<-(n*16.5)
				Escribir "El precio es " p
			SiNo
				Si n<40 Entonces
					p<-(n*13.2)
					Escribir "El precio es " p
				SiNo
					Escribir "Cotizar carga"
				Fin Si
			Fin Si
		Fin Si
	Fin Si
	
FinAlgoritmo
