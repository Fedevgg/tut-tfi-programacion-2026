// Adivinar
// Generar un programa donde a partir de un n�mero aleatorio
// entre 1 y 25, permita al usuario adivinarlo. Indicando, adem�s, si
// el n�mero en cada intento es cercano est� alejado o es correcto.
// (Usar la funci�n Azar)

Algoritmo Adivinar
	Definir numeroSecreto, intento, distanciaFria Como Entero
	numeroSecreto <- Azar(25)
	distanciaFria <- 5
	Repetir
		Escribir "Ingrese un numero: "
		Leer intento
		Si intento = numeroSecreto Entonces
			Escribir "Felicitaciones! Adivinaste el numero."
		Sino
			Si Abs(intento - numeroSecreto) <= distanciaFria Entonces
				Escribir "Caliente."
			Sino
				Escribir "Frio."
			FinSi
			Si intento < numeroSecreto Entonces
				Escribir "El numero es mayor."
			Sino
				Escribir "El numero es menor."
			FinSi
		FinSi
	Hasta Que intento = numeroSecreto
FinAlgoritmo
