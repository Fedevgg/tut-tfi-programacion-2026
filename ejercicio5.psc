// Tabla de multiplicar
// Generar un programa que permita visualizar la tabla de multiplicar de
// un número "n" (n X 20) . (Donde el usuario debe ingresar el valor n)

Algoritmo TablaDeMultiplicar

	Definir numero Como Entero
	Escribir "Ingrese el número para la tabla de multiplicar: "
	Leer numero
	ImprimirTabla(numero)
FinAlgoritmo

SubProceso ImprimirTabla(numero)
	Definir i Como Entero
	Para i <- 1 Hasta 20 Hacer
		Escribir numero, " x ", i, " = ", numero * i
	FinPara
FinSubProceso
