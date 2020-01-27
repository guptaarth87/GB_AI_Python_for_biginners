"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
 Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict. 
"""
# my_dict = dict(январь='зима', февраль='зима', март='весна', апрель='весна', май='весна', июнь='лето', июль='лето',
#                август='лето', сентябрь='осень', октябрь='осень', ноябрь='осень', декабрь='зима')
my_dict = dict(winter=(12, 1, 2), spring=(3, 4, 5), summer=(6, 7, 8), autumn=(9, 10, 11))

user_input = int(input("Enter month's number:"))

if user_input>=0 and user_input<=12:
    for key in my_dict:

        if my_dict[key].count(user_input)==True:
            print(f"It's {key} time!")
            break
else:
    print(f"Suppose you had entered wrong month's number: {user_input}.\nIt should be from 1 to 12." )
