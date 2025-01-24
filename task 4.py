import random
from time import time

list = [random.randint(10, 1000) for _ in range(500)]

def bubble_sort(list):
    n = len(list)
    for _ in range(n - 1):
        for __ in range(n - 1 - _):
            if list[__] > list[__ + 1]:
                list[__], list[__ + 1] = list[__ + 1], list[__]
    return list[-1]

def crunching_sort(list):
    num = 0
    for _ in range(len(list) - 1):
        if list[_] > num:
            num = list[_]
    return num

tic = time()
print(bubble_sort(list))
print('Сортировка "пузырком", время работы:', time() - tic)

tic = time()
print(crunching_sort(list))
print('Сортировка перебором, время работы:', time() - tic)