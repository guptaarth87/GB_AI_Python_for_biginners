"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
res_list = []

with open('data/task4.data', 'r') as f:
    for line in f:
        str_in_data = line.split()
        str_in_data[0] = num_dict[str_in_data[0]]
        res_list.append(' '.join(str_in_data))

with open('data/task4_out.data', 'w') as f:
    for item in res_list:
        f.write(item + '\n')

print('Done. Check data/task4_out.data.')
