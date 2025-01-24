from random import randint

n = int(input('Введите размерность матрицы: '))

matrix = [[randint(1, 100) for _ in range(n)] for __ in range(n)]

matrix.insert(0, matrix[-1])
matrix.pop(-1)

print(matrix)