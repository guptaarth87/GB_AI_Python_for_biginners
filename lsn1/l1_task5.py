"""
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
 (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
  Выведите соответствующее сообщение.
  Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

revenue=float(input('Enter revenue:'))
costs=float(input('Enter costs:'))
margin=revenue-costs

if margin>0:
    print("It's OK!")
    profit_margin=revenue/margin
    team=int(input('Enter number of employees:'))
    print(f'Profit margin is {round(profit_margin,2)}.\n Margin per employee {round(margin/team,2)}.')
elif margin<0:
    print("It's nOK!")
else:
    print('Margin is Zero. You should do something.')