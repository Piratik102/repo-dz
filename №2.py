# Задание №2

time_in = int(input('Введите время в секундах: '))

seconds = int(time_in % 60)
time_m = (time_in - seconds)/60

minutes = int(time_m % 60)
time_h = (time_m - minutes)/60

hours = int(time_h % 24)
days = int((time_h-hours)/24)

# if seconds < 10:
#     seconds = str(seconds)
#     seconds = '0' + seconds
#
# if minutes < 10:
#     minutes = str(minutes)
#     minutes = '0' + minutes
#
# if hours < 10:
#     hours = str(hours)
#     hours = '0' + hours


if seconds < 10:
    seconds = f'0{seconds}'

if minutes < 10:
    minutes = f'0{minutes}'

if hours < 10:
    hours = f'0{hours}'

print(hours, ':', minutes, ':', seconds)

if days > 1:
    print('Кол-во дней: ', days)



