"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка.

"""
user_in=None
with open('data/task1.data', 'w') as f:
    while True:
        user_in = input()+'\n'
        if user_in=='\n':
            break
        else:
            f.write(user_in)

print('Finished.')
