Algoritmo Que_factores_multiplicados_permiten_llegar_a_n
	Leer n
	m<-1
	c<-1
	r<-0
	Mientras m<>(n/2) Hacer
		Mientras c <= n Hacer
			r<-m*c
			Si r=n Entonces
				Si c>m Entonces
					Escribir m " x " c
					c<-c+1
				SiNo
					c<-c+1
				Fin Si
			SiNo
				c<-c+1
			Fin Si
		Fin Mientras
		c<-1
		m<-m+1
	Fin Mientras
	
FinAlgoritmo
