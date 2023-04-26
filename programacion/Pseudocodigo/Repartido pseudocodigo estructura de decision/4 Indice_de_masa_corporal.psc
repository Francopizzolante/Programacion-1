Algoritmo Indice_de_masa_corporal
	Escribir "Ingrese peso y altura"
	Leer peso, altura
	a<-altura^2
	i<-peso/a
	Si i<18.5 Entonces
		Escribir "Bajo Peso"
	SiNo
		Si i>=18.5 y i<=24.9 Entonces
			Escribir "Peso adecuado"
		SiNo
			Si i>24.9 y i<=29.9 Entonces
				Escribir "Sobrepeso"
			SiNo
				Escribir "Obesidad" 
			Fin Si
		Fin Si
	Fin Si
FinAlgoritmo
