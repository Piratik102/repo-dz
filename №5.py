# Задание №5

revenue = float(input('Введите сумму выручки: '))
costs = float(input('Введите сумму издержек: '))

profit = revenue - costs

if profit > 0:
    print('Фирма работает в прибыль')
    print('Рентабельность выручки составляет: ',int(profit/revenue*100), ' %')   # в процентах
    com = int(input('Введите кол-во сотрудников фирмы: '))
    print('Прибыль на одного сотрудника состовляет: ', int(profit/com), ' рублей')
elif profit == 0:
    print('Выручка равна издержкам')
else:
    print('Фирма работает в убыток')
