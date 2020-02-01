"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы.
 Реализовать вывод данных о пользователе одной строкой.
"""


def user_folder(name, surname, year, city, email, phone):
    print(f'{surname} {name}:\n {year} годa рождения, проживает в {city}, Email: {email}, телефон:{phone}.\n')


while True:
    print('Введите данные о пользователе:')
    name = input('1) имя:')
    surname = input('2) фамилия:')
    year = input('3) год рождения:')
    city = input('4) город проживания:')
    email = input('5) email:')
    phone = input('6) телефон:')

    user_folder(name, surname, year, city, email, phone)
