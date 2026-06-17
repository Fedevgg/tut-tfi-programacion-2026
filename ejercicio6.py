"""
Pirámide
Escribir un programa donde el usuario deba ingresar un número y
pueda generarse una pirámide de números naturales, con altura igual
al número ingresado. (Cada escalón de la pirámide se conforma de
números naturales, y en cada uno de ellos, se agrega un elemento)
"""


def print_pyramid(height: int) -> None:
    """
    Prints a pyramid of natural numbers, based on a given height
    Args:
        height (int): The height of the pyramid
    """
    counter = 1
    for row in range(1, height + 1):
        spaces = " " * (height - row)
        numbers = []
        for _ in range(row):
            numbers.append(str(counter))
            counter = 1 if counter == 9 else counter + 1
        print(spaces + " ".join(numbers))


def main():
    height = int(input("Ingrese la altura de la pirámide: "))
    print_pyramid(height)


if __name__ == "__main__":
    main()
