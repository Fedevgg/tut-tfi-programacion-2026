"""
Invertir
Este ejercicio debe solicitar al usuario que ingrese una
cadena de texto o frase, y que la muestre invertida
"""


def reverse_text(text: str) -> str:
    """
    Uses python's slice notation to reverse the text
    Args:
        text (str): The text to reverse
    Returns:
        str: The reversed text
    """
    return text[::-1]


def main():
    text = input("Ingrese una cadena de texto o frase: ")
    print(f"La cadena invertida es: {reverse_text(text)}")


if __name__ == "__main__":
    welcome_message = "Ejercicio 2: Inversor de texto"
    print(welcome_message)
    print(reverse_text(welcome_message))
    main()
