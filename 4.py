# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input('Введите число: '))
# b = ''
# while n > 0:
#     b = str(n % 2) + b
#     n = n // 2
# print(int(b))

def bin(x):
    bin = ''
    while x > 0:
        bin = str(x % 2) + bin
        x = x//2
    return bin

dec = int(input('Введите число: '))
print(bin(dec))