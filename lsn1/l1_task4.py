"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

start_number = int(input('Enter positive integer number:'))
m = start_number%10
a = start_number//10
# print(f'm={m}, a={a}')
while a > 0:
    if a%10 > m:
        m = a%10
    a = a//10
    # print(f'WC: m={m}, a={a}')
print(f'The biggest digit is {m}.')