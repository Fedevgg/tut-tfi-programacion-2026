// Contador de vocales
// Este ejercicio debe solicitar al usuario que ingrese una palabra o
// frase. Para que sea analizada y retorne cuántas vocales (tanto
// mayúsculas como minúsculas) contiene, mostrando el resultado
// de la salida

Algoritmo ContadorDeVocales
	Definir texto, caracter Como Cadena
	Definir i, cantidad Como Entero
	cantidad <- 0
	Escribir "Ingrese una palabra o frase: "
	Leer texto
	Para i <- 1 Hasta Longitud(texto) Hacer
		caracter <- Subcadena(texto, i, i)
		Si caracter = "a" O caracter = "e" O caracter = "i" O caracter = "o" O caracter = "u" O caracter = "A" O caracter = "E" O caracter = "I" O caracter = "O" O caracter = "U" Entonces
			cantidad <- cantidad + 1
		FinSi
	FinPara
	Escribir "La cantidad de vocales en la frase es: ", cantidad
FinAlgoritmo
