"""
Contador de vocales
Este ejercicio debe solicitar al usuario que ingrese una palabra o
frase. Para que sea analizada y retorne cuántas vocales (tanto
mayúsculas como minúsculas) contiene, mostrando el resultado
de la salida
"""

VOWELS = "aeiou"


def count_vowels(text: str) -> int:
    """
    Counts the number of vowels in the text
    Args:
        text (str): The text to count the vowels
    Returns:
        int: The number of vowels in the text
    """
    text = text.lower()
    return sum(1 for char in text if char in VOWELS)


def main():
    text = input("Ingrese una palabra o frase: ")
    print(f"La cantidad de vocales en la frase es: {count_vowels(text)}")


if __name__ == "__main__":
    main()
