"""
Suma de Matrices
Este ejercicio debe permitir cargar dos matrices y calcular
la suma de ambas, mostrando el resultado como una matriz
"""


def load_matrix(rows: int, columns: int) -> list(list[float]):
    """
    Loads a matrix from the user
    Args:
        rows (int): The number of rows in the matrix
        columns (int): The number of columns in the matrix
    Returns:
        list: The matrix
    """
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            value = float(input(f"Ingrese el valor para la posición {i+1},{j+1}: "))
            row.append(value)
        matrix.append(row)
    return matrix


def print_matrix(matrix: list(list[float])) -> None:
    """
    Prints a matrix
    Args:
        matrix (list): The matrix to print
    """
    for row in matrix:
        print(row)


def sum_matrices(
    matrix1: list(list[float]), matrix2: list(list[float])
) -> list(list[float]):
    """
    Sums two matrices
    Args:
        matrix1 (list): The first matrix
        matrix2 (list): The second matrix
    Returns:
        list: The sum of the two matrices
    """
    matrix3 = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        matrix3.append(row)
    return matrix3


def main():
    rows = int(input("Ingrese el número de filas de las matrices: "))
    columns = int(input("Ingrese el número de columnas de las matrices: "))
    print("Ingrese los valores de la primera matriz:")
    matrix1 = load_matrix(rows, columns)
    print("Ingrese los valores de la segunda matriz:")
    matrix2 = load_matrix(rows, columns)
    print("La suma de las matrices es:\n")
    print_matrix(sum_matrices(matrix1, matrix2))


if __name__ == "__main__":
    main()
