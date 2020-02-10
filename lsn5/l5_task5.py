"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randrange
from functools import reduce


random_num_list=[randrange(10,99) for i in range(3)]
print(f'Random generated list SUM {random_num_list}  = {sum(random_num_list)}')

with open('data/task5_in.data','w') as f:
    for num in random_num_list:
        f.write(str(num)+' ')
    print(f'Randomly generated list has written down to data/task5_in.data.\n')

with open('data/task5_in.data', 'r') as f:
    for line in f:
        file_num_list=line.split()
    print(f'It had read from data/task5_in.data list of number.')

print(f'Number list SUM {file_num_list}  = {sum(map(int,file_num_list))}\n')
print('All done.')