"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (> 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

with open('data/task3.data','r') as f:
    data_list=f.readlines()


user_list=[]
min_salary_list=[]
total_salary_sum=0

for each in data_list:
    each=each.split()
    user_list.append(each)

for num, user in enumerate(user_list):
    # print(user[1])
    if float(user[1])<20000:
        min_salary_list.append(user)
    total_salary_sum+=float(user[1])


print(f'Среднаяя з/п равна {total_salary_sum/len(user_list)}.')
print(f'Сотрудники с з/п менее 20 000:')
for num,item in enumerate(min_salary_list,start=1): print(num, item[0],item[1])