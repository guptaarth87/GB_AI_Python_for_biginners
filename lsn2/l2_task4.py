"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
 Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
 Если в слово длинное, выводить только первые 10 букв в слове. 
"""
user_input = input('Enter a sentence:')

user_list = list(user_input.split())

for num, item in enumerate(user_list):
    if len(item) > 10:
        print(num, '%.10s' % item)
    else:
        print(num, item)
