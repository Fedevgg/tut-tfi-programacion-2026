"""
Triángulo
Escribir un programa que calcule el área de un triángulo dados su
base y su altura. (Donde el usuario debe ingresar los datos)
"""


def calculate_triangle_area(base: float, height: float) -> float:
    """
    Calculates the area of a triangle
    Args:
        base (float): The base of the triangle
        height (float): The height of the triangle
    Returns:
        float: The area of the triangle
    """
    return (base * height) / 2


def main():
    base = float(input("Ingrese la base del triángulo: "))
    height = float(input("Ingrese la altura del triángulo: "))
    print(f"El área del triángulo es: {calculate_triangle_area(base, height)}")


if __name__ == "__main__":
    main()
