# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math


def spisok(x):
    for i in range(len(x)):
        x[i] = round(x[i]-math.floor(x[i]), 2)

def difference(x):
    max_x = x[0]
    min_x = x[0]
    for i in range(len(x)):
        if max_x < x[i]:
            max_x = x[i]
        elif min_x > x[i] and x[i] != 0:
            min_x = x[i]
    return max_x-min_x

num = [1.1, 1.2, 3.1, 5, 10.01]
spisok(num)
print(difference(num))