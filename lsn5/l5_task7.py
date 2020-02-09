"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
 название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
 Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
 Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json

a_profit=0
company_profit = 0
dict1 = {}
result_list = []

with open('data/task7.data', 'r') as f:
    for line in f:
        temp_list = line.split()
        company_profit = float(temp_list[2]) - float(temp_list[3])

        if company_profit > 0:
            dict1.update({temp_list[0]: company_profit})
            a_profit+=company_profit


result_list.append(dict1)
result_list.append({'average_profit':a_profit})
print(result_list)

with open('data/task7.json','w') as f:
    json.dump(result_list,f)

print('All done.')
