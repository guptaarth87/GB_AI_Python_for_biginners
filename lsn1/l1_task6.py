"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
 Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
  Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат: 
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

first_day_result = float(input('Input result of first day training (km):'))
target_distance = float(input('Input target distance (km):'))

number_training = 1
distance=first_day_result

while distance <= target_distance:
    number_training += 1
    distance += distance * 0.1

print(f'The day of target distance is {number_training}th.')
