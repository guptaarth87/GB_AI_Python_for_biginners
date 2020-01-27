"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
 Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict. 
"""

my_tuple = (('зима', (1, 'январь'), (2, 'февраль'), (12, 'декабрь')), ('весна', (3, 'март'), (4, 'апрель'), (5, 'май')),
            ('лето', (6, 'июнь'), (7, 'июль'), (8, 'август')),
            ('осень', (9, 'сентябрь'), (10, 'октябрь'), (11, 'ноябрь')))

my_dict = dict(зима=(12, 1, 2), весна=(3, 4, 5), лето=(6, 7, 8), осень=(9, 10, 11))

user_input = int(input("Введите номер месяца:"))

if user_input >= 0 and user_input <= 12:

    for season in my_tuple:
        # print(f'Print season data:{season}, {len(season)}')
        for month in season:
            # print(f'Print MONTH data:{month}, {len(month)}')
            if month[0] == user_input:
                print(f"Вы ввели {user_input}: это {month[1]} и {season[0]}.\n Использовался список:{my_tuple}")
                break

    for key in my_dict:
        if my_dict[key].count(user_input) == True:
            print(f"Вы ввели {user_input}: это {key}.\n Использовался словарь:{my_dict}")
            break


else:
    print(f"Suppose you had entered wrong month's number: {user_input}.\nIt should be from 1 to 12.")
