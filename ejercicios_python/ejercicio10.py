"""Promedio
Este ejercicio debe permitir ingresar una cantidad finita (hasta 10)
de números y luego calcular el promedio. El programa debe
finalizar cuando el usuario ingrese un valor negativo, el mismo no
se debe incluir en el promedio
"""


def calculate_average(numbers: list[float]) -> float:
    """
    Calculates the average of a list of numbers
    Args:
        numbers (list[float]): The list of numbers
    Returns:
        float: The average of the numbers
    """
    return sum(numbers) / len(numbers)


def main():
    numbers = []
    print(
        "Ingrese hasta 10 números para calcular el promedio, o uno negativo para finalizar:"
    )
    while len(numbers) < 10:
        number = float(input("Ingrese un número: "))
        if number < 0:
            break
        if len(numbers) >= 10:
            print("Se han ingresado 10 números, no se puede ingresar más.")
            break
        numbers.append(number)
    print(f"El promedio de los números es: {calculate_average(numbers)}")


if __name__ == "__main__":
    main()
