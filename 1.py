# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def two_element_sum(list):
    res = 0
    for i in range(len(list)):
        if i % 2 != 0:
            res += list[i]
    return res

my_list = [2, 3, 5, 9, 3]

print(two_element_sum(my_list))