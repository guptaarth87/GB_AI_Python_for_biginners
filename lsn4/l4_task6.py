"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from sys import argv
from itertools import count, cycle


def test_A(x, y):
    for num in count(int(x)):
        if num < int(y):
            print(num)
        else:
            return 'Done test A.'


def test_B(x, y):
    i = 0
    for item in cycle(x):
        i += 1
        if i < int(y):
            print(item)
        else:
            return 'Done test B.'


# list1=[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

type_iter, long_iter, max_iter = argv[1:]
print(argv[1:])

if type_iter == 'A':
    print(test_A(long_iter, max_iter))
elif type_iter == 'B':
    print(test_B(long_iter, max_iter))
else:
    print('You should choose option A or B.')
