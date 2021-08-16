# Задание №1

a = 57
print(a)

a = 54
a = float(a)
print(a)

a = 'my_text'
print(a)

a = True
print(a)

a = float(input('Введите любое число: '))
if a % 1 == 0:
    a = int(a)
    print('Вы ввели целое число: ', a)
else:
    print('Вы ввели нецелое число: ', a)

b = input('Введите ваше имя: ')
print('Приятно познакомиться, ', b)

