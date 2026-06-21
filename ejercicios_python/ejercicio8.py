"""Adivinar
Generar un programa donde a partir de un número aleatorio
entre 1 y 25, permita al usuario adivinarlo. Indicando, además, si
el número en cada intento es cercano está alejado o es correcto.
(Usar la función Azar)
"""

import random

COLD = 5


def guess_number() -> None:
    """
    Guesses the number
    """
    number = random.randint(1, 25)
    while True:
        guess = int(input("Ingrese un número: "))
        if guess == number:
            print("¡Felicitaciones! Adivinaste el número.")
            break
        elif abs(guess - number) <= COLD:
            print("Caliente.")
        else:
            print("Frío.")
        if guess < number:
            print("El número es mayor.")
        else:
            print("El número es menor.")


def main():
    guess_number()


if __name__ == "__main__":
    main()
