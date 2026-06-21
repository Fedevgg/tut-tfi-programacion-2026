// Suma de Matrices
// Este ejercicio debe permitir cargar dos matrices y calcular
// la suma de ambas, mostrando el resultado como una matriz

Algoritmo SumaDeMatrices
	
	Definir filas, columnas, i, j Como Entero
	Definir fila Como Cadena
	Definir m1, m2, m3 Como Real
	
	// Se podría validar que la suma sea válida usando las
	// dimensiones pero escapa el alcance del pedido
	Escribir "Ingrese el número de filas de las matrices: "
	Leer filas
	Escribir "Ingrese el número de columnas de las matrices: "
	Leer columnas
	
	Dimension m1(filas, columnas)
	Dimension m2(filas, columnas)
	Dimension m3(filas, columnas)
	
	Escribir "Ingrese los valores de la primera matriz:"
	Para i <- 1 Hasta filas Hacer
		Para j <- 1 Hasta columnas Hacer
			Escribir "Ingrese el valor para la posición ", i, ",", j, ": "
			Leer m1[i, j]
		FinPara
	FinPara
	Escribir "Ingrese los valores de la segunda matriz:"
	Para i <- 1 Hasta filas Hacer
		Para j <- 1 Hasta columnas Hacer
			Escribir "Ingrese el valor para la posición ", i, ",", j, ": "
			Leer m2[i, j]
		FinPara
	FinPara
	Para i <- 1 Hasta filas Hacer
		Para j <- 1 Hasta columnas Hacer
			m3[i, j] <- m1[i, j] + m2[i, j]
		FinPara
	FinPara
	Escribir "La suma de las matrices es:"
	Para i <- 1 Hasta filas Hacer
		fila <- ""
		Para j <- 1 Hasta columnas Hacer
			fila <- fila + ConvertirATexto(m3[i, j])
			Si j < columnas Entonces
				fila <- fila + " "
			FinSi
		FinPara
		Escribir fila
	FinPara
FinAlgoritmo
