import random

def generate_matrix(n):
    return [[random.randint(0, 100) for _ in range(n)] for _ in range(n)]

def bubble_sort_column(matrix, column):
    n = len(matrix)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if matrix[j][column] > matrix[j + 1][column]:
                matrix[j][column], matrix[j + 1][column] = matrix[j + 1][column], matrix[j][column]

def sort_matrix_by_columns(matrix):
    n = len(matrix)
    for column in range(n):
        bubble_sort_column(matrix, column)

def print_matrix(matrix):
    for row in matrix:
        print(row)

n = int(input())
matrix = generate_matrix(n)
print("Исходная матрица:")
print_matrix(matrix)

sort_matrix_by_columns(matrix)
print("\nМатрица после сортировки по столбцам:")
print_matrix(matrix)