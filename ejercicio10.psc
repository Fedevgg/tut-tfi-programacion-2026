// Promedio
// Este ejercicio debe permitir ingresar una cantidad finita (hasta 10)
// de n�meros y luego calcular el promedio. El programa debe
// finalizar cuando el usuario ingrese un valor negativo, el mismo no
// se debe incluir en el promedio

Algoritmo Promedio
	Definir numero, suma, cantidad, promiedo Como Real
	suma <- 0
	cantidad <- 0
	Escribir "Ingrese hasta 10 numeros para calcular el promedio, o uno negativo para finalizar:"
	Repetir
		Escribir "Ingrese un numero: "
		Leer numero
		Si numero >= 0 Entonces
			suma <- suma + numero
			cantidad <- cantidad + 1
		FinSi
	Hasta Que numero < 0 O cantidad = 10
	Si cantidad > 0 Entonces
		promiedo <- suma / cantidad
		Escribir "El promedio de los numeros es: ", promiedo
	FinSi
FinAlgoritmo
