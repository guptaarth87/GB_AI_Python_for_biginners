"""
Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и
 сохраните в переменные, выведите на экран.
"""

x = int(input("Enter integer number:"))
y = float(input("Enter float number:"))
str1 = input("Enter string:")
str2 = input("Enter another string:")

print(f'Your input are:\n{x, type(x)},\n{y, type(y)}\n{str1, type(str1)}\n{str2, type(str2)}')
