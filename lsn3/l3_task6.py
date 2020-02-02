"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
 но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
 Каждое слово состоит из латинских букв в нижнем регистре.
 Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
 Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(x):
    y = ''
    x[0] = x[0].title()
    for letter in x:
        y = y + letter
    return (y + ' ')


user_words = input('Enter a string:').split()
result_str = ''

for word in user_words:
    lword = list(word)
    result_str = result_str + int_func(lword)

print(result_str)
