Algoritmo Que_factores_multiplicados_permiten_llegar_a_n
	Leer n
	c<-1
	r<-0
	Para m<-1 Hasta n/2 Con Paso 1 Hacer
		Para c<-1 Hasta n Con Paso 1 Hacer
			r<-m*c
			Si r=n Entonces
				Si c>m Entonces
					Escribir m " x " c
					c<-c+1
				SiNo
					c<-c+1
				Fin Si
			SiNo
			Fin Si
		Fin Para
	Fin Para
FinAlgoritmo
