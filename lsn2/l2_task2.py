"""
Для списка реализовать обмен значений соседних элементов,
 т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
 Для заполнения списка элементов необходимо использовать функцию input().
"""

user_list = list(input('Enter string:'))
print(f'Original list is {user_list}.')

user_len = len(user_list)
if user_len % 2 != 0:
    user_len -= 1

for i in range(0, user_len, 2):
    user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]

print(f'Transformed list is {user_list}.')
