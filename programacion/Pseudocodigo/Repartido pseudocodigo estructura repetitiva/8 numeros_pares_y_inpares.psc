Algoritmo numeros_pares_y_inpares
	p<-0
	i<-0
	n<-0
	Mientras n<>(-1) Hacer
		Leer n
		Para c<-0 Hasta n+1 Con Paso 2 Hacer
			Si c>n Entonces
				i<-i+1
			SiNo
				Si c=n Entonces
					p<-p+1
				SiNo
				Fin Si
			Fin Si
		Fin Para
	Fin Mientras
	i<-i-1
	Escribir "Se ingresaron " p " pares" " y " i " impares"
FinAlgoritmo
