"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

user_time = int(input('Enter time in secs:'))


hours = user_time // 3600
minutes = user_time % 3600 // 60
secs = user_time % 60

print(f'Result is hh:mm:ss -> {hours}:{minutes}:{secs}')
