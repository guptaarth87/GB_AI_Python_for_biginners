"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


def sum_2_max(a, b, c):
    try:
        list = [int(a), int(b), int(c)]

        max1 = max(list)
        list.remove(max1)
        max2 = max(list)

        return max1 + max2
    except:
        print('Wrong data.')
        return None


while True:
    print('Enter 3 number:')
    a = input('A=')
    b = input('B=')
    c = input('C=')

    result=sum_2_max(a, b, c)
    print(f'Result is {result}.\n')
