# Задание №6

beginning = float(input('Введите длину пути, с которой вы хотите начать тренировки, в км: '))
a = beginning
finish = float(input('Введите длину пути, до которой вы хотите продолжать увеличивать длину пробежки, в км: '))
i = 1

if (finish > beginning) and (beginning * finish > 0):
    while finish > a:
        # print('День ', i, '-й длина пути', round(a, 2))
        i += 1
        a = a * 1.1

    # print('День ', i, '-й длина пути', round(a, 2))

    print('На ', i, '-й день длина пути стала составлять не менее ', finish, ' км.')
else:
    print('Проверьте правильность ввода данных')