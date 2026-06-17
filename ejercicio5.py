"""
Tabla de multiplicar
Generar un programa que permita visualizar la tabla de multiplicar de
un número “n” (n X 20) . (Donde el usuario debe ingresar el valor n)
"""


def print_multiplication_table(number: int) -> None:
    """
    Prints the multiplication table of a number
    Args:
        number (int): The number to print the multiplication table
    """
    for i in range(1, 21):
        print(f"{number} x {i} = {number * i}")


def main():
    number = int(input("Ingrese el número para la tabla de multiplicar: "))
    print_multiplication_table(number)


if __name__ == "__main__":
    main()
