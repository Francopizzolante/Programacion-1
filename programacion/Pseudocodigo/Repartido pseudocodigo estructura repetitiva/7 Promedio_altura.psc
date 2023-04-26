Algoritmo Promedio_altura
	Escribir "Ingrese cuantas alturas va a ingresar"
	Leer n
	m<-0
		Para c<-1 Hasta n Con Paso 1 Hacer
			Escribir "Ingrese una altura"
			Leer a
			Si a>m Entonces
				m=a
			SiNo
			Fin Si
		Fin Para
		Imprimir "la altura mas alta es " m
FinAlgoritmo