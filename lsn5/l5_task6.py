"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
 практических и лабораторных занятий по этому предмету и их количество.
 Важно, чтобы для каждого предмета не обязательно были все типы занятий.
 Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика:   100(л)   50(пр)      20(лаб).
     Физика:   30(л)    —           10(лаб)
Физкультура:   —        30(пр)      —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

file_list = []


def do_all_things(l):
    user_dict = {}

    for item in file_list:
        number = ''
        sum_number = 0
        for num, word in enumerate(item):
            if num != 0:
                for id_char, char in enumerate(word):

                    if char.isdigit():
                        number += char
                    elif char == '(':
                        sum_number += int(number)
                        # print(f'sum_number={sum_number}, number={number}')
                        number = ''
                        user_dict.update({item[0]: sum_number})

    return user_dict


with open('data/task6.data', 'r') as f:
    for line in f:
        file_list.append(line.split())

print(do_all_things(file_list))
