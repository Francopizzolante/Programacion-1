Algoritmo Ejercisio_2
	mv<-3000
	mvc<-0
	c<-0
	t<-0
	Mientras c<=30 y t<3000 Hacer
		Escribir "Ingrese los minutos"
		Leer m
		Escribir "Ingrese los segundos"
		Leer s
		c<-c+1
		t<-t+s+(m*60)
		Si mv>s+(m*60) Entonces
			mv=s+(m*60)
			mvc<-c
		Fin Si

	Fin Mientras
	p<-t/c
	Escribir "El tiempo total de carrera es ", t
	Escribir "El promedio de vuelta es ", p
	Escribir "El mejor tiempo de vuelta fue ", (mv), " en la vuelta ", mvc
FinAlgoritmo
