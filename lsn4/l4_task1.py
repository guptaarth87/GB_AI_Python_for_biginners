"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def salary(a, b, c):
    """ Пареметры скрипта: (Фамилия) (выработка в часах) (ставка в час) (премия)"""
    result = float(a) * float(b) + float(c)
    return result


surname, total_work_hours, cost_per_hour, bonus = argv[1:]
print(f'{surname} get {salary(total_work_hours, cost_per_hour, bonus)} rubles salary.')
