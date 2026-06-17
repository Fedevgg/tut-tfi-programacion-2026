"""Interés
Escribir un programa que solicite al usuario ingresar el capital y el
tiempo, y luego, permita calcular el interés simple.
Nota: La tasa de interés se encuentra precargada en el ejercicio y
debe ser mostrada al usuario.
Fórmula: interés = capital * tasa * tiempo
"""

INTEREST_RATE = 0.10  # 10%


def calculate_interest(capital: float, time: float) -> float:
    """
    Calculates the interest
    Args:
        capital (float): The capital
        time (float): The time
    Returns:
        float: The interest
    """
    return capital * time * INTEREST_RATE


def main():
    capital = float(input("Ingrese el capital: "))
    time = float(input("Ingrese el tiempo (en meses): "))
    print(f"El monto final con intereses es: ${calculate_interest(capital, time):.2f}")


if __name__ == "__main__":
    main()
