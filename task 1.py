from time import time
from random import randint

list = [randint(1, 1000) for _ in range(500)]

def bubble_sort(list):
    n = len(list)
    for _ in range(n - 1):
        for __ in range(n - 1 - _):
            if list[__] > list[__ + 1]:
                list[__], list[__ + 1] = list[__ + 1], list[__]
    return list

tic = time()
print(bubble_sort(list))
print('Сортировка "пузырком", время работы:', time() - tic)

tic = time()
print(sorted(list))
print('Сортировка встроенным метедом sorted, время работы:', time() - tic)



