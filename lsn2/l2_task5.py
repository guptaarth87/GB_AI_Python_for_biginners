"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
 У пользователя необходимо запрашивать новый элемент рейтинга.
 Если в рейтинге существуют элементы с одинаковыми значениями,
  то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2. 
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

"""
my_list = [10, 7, 2, 3, 5, 3]
my_list.sort(reverse=True)

print(my_list)
while True:
    user_input = int(input('>>'))
    if user_input in my_list:
        x = my_list.index(user_input)
        y = my_list.count(user_input)
        my_list.insert((x + y), user_input)
    elif user_input > my_list[0]:
        my_list.insert(0, user_input)
    elif user_input < my_list[-1]:
        my_list.insert(len(my_list), user_input)
    else:
        for item in range(len(my_list) - 1, -1, -1):
            if my_list[item] < user_input <= my_list[item - 1]:
                my_list.insert(item, user_input)
    print(my_list)
