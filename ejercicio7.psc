// Interés
// Escribir un programa que solicite al usuario ingresar el capital y el
// tiempo, y luego, permita calcular el interés simple.
// Nota: La tasa de interés se encuentra precargada en el ejercicio y
// debe ser mostrada al usuario.
// Fórmula: interés = capital * tasa * tiempo

Algoritmo Interes
	Definir capital, tiempo, tasa, interes Como Real
	tasa <- 0.10
	Escribir "Tasa de interés: 10%"
	Escribir "Ingrese el capital: "
	Leer capital
	Escribir "Ingrese el tiempo (en meses): "
	Leer tiempo
	interes <- capital * tiempo * tasa
	Escribir "El monto final con intereses es: $", interes
FinAlgoritmo
