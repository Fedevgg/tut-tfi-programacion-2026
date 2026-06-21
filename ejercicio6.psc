// Pirámide
// Escribir un programa donde el usuario deba ingresar un número y
// pueda generarse una pirámide de números naturales, con altura igual
// al número ingresado. (Cada escalón de la pirámide se conforma de
// números naturales, y en cada uno de ellos, se agrega un elemento)

Algoritmo Piramide
	Definir altura Como Entero
	Escribir "Ingrese la altura de la pirámide: "
	Leer altura
	Definir fila, col, espacio, contador Como Entero
	Definir linea Como Cadena

	contador <- 1
	Para fila <- 1 Hasta altura Hacer
		linea <- ""

		// Para evitar un corrimiento de la base de la pirámide
		// Se verifica que la fila sea mayor a 0
		Si altura - fila > 0 Entonces
			Para espacio <- 1 Hasta altura - fila Hacer
				linea <- linea + " "
			FinPara
		FinSi
		Para col <- 1 Hasta fila Hacer
			linea <- linea + ConvertirATexto(contador)
			Si col < fila Entonces
				linea <- linea + " "
			FinSi
			// Para simplificar el manejo del ancho
			// Reinicio el contador y mantengo solo una unidad de entero
			Si contador = 9 Entonces
				contador <- 1
			Sino
				contador <- contador + 1
			FinSi
		FinPara
		Escribir linea
	FinPara
FinAlgoritmo
