Algoritmo sin_titulo
	Escribir "Ingrese la poblacion y el area"
	Leer p
	Leer a
	n = p/a
	Si n<=100 Entonces
		Escribir "La poblacion es baja"
	SiNo
		Si n>100 y n<=150 Entonces
			Escribir "La poblacion es medio"
		SiNo
			Si n>150 Entonces
				Escribir "La poblacion es alta"
			FinSi
		FinSi
	FinSi
FinAlgoritmo
