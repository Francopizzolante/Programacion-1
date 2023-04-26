Algoritmo calcular_sueldo
	Escribir "Ingresar sueldo y hs trabajadas"
		Leer s
		Leer h
		t<-0
		Si h>40 Entonces
			h<-(h-40)
			t<-(s*40)+(s*2*h)
		SiNo
			t<-s*h
		Fin Si
		Escribir "el sueldo es " t
FinAlgoritmo
