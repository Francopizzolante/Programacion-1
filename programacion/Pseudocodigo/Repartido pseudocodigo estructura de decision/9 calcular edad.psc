Algoritmo edad
	Escribir "Ingrese la Fecha de nacimiento de manera que escriva el dia luego enter luego el mes y luego el año"
	Leer d1, m1, a2
	Escribir "Ingrese la Fecha actual de la misma manera"
	Leer d2, m2, a2
	Si m2<m1 Entonces
		e<-a2-a1-1
	SiNo
		Si d2<d1 Entonces
			e<-a2-a1-1
		SiNo
			e<-a2-a1
		Fin Si
	Fin Si
	Escribir e
	
FinAlgoritmo
