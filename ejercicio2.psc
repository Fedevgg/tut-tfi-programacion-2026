// Invertir
// Este ejercicio debe solicitar al usuario que ingrese una
// cadena de texto o frase, y que la muestre invertida

Algoritmo Invertir
	Definir texto, invertido, caracter Como Cadena
	Definir i Como Entero
	invertido <- ""
	Escribir "Ingrese una cadena de texto o frase: "
	Leer texto
	Para i <- Longitud(texto) Hasta 1 Con Paso -1 Hacer
		caracter <- Subcadena(texto, i, i)
		invertido <- invertido + caracter
	FinPara
	Escribir "La cadena invertida es: ", invertido
FinAlgoritmo
