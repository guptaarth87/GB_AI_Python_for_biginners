"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def my_div(a,b):
    try:
        return float(a)/float(b)
    except:
        print("Something is wrong. Maybe it is diviion by Zero or symbol's input.")
        return None


while True:
    print('\nLet try to divide A by B.')
    a=input('Enter A:')
    b=input('Enter B:')

    div_result=my_div(a,b)
    print(f'A/B={div_result}')
