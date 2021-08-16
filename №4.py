# Задание №4

number = int(input('Введите любое число: '))
a = number
max = 0

while number > 0:
    n = number % 10
    if max < n:
        max = n

    if max == 9:
        break
    number = number // 10


print('Максимальная цифра в числе ', a,' равна: ', max)

