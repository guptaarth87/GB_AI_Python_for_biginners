"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
 name, surname, position (должность), income (доход).
 Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
  оклад и премия, например, {"wage": wage, "bonus": bonus}.
   Создать класс Position (должность) на базе класса Worker.
   В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
    (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
 атрибутов, вызвать методы экземпляров).
"""


class Worker:

    name = str()
    surname = str()
    position = str()
    _income = dict({"wage": int(), "bonus": int()})

    def __init__(self, name, surname, position, wage):
        self.name = name
    #     self.surname = surname
    #     self.position = position
    #     self._income.update({"wage": int(wage)})
    #     print(self.name, self.surname, self.position, self._income['wage'])


class Position(Worker):

    def __init__(self,name,surname,position,wage):
        super().__init__(name,surname,position,wage)
        self.name = name
        self.surname = surname
        self.position = position
        self._income.update({"wage": int(wage)})
        # self._income= wage
        print(self.name, self.surname, self.position, self._income['wage'])
        # print(self.name, self.surname, self.position, self._income)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self, b):
        self._income['bonus'] = b
        return int(self._income['wage']) + int(self._income['bonus'])
        # self.bonus = b
        # return int(self._income) + int(self.bonus)


wrk1 = Position('John', 'Deer', 'driver', '1')
wrk2 = Position('Ringo', 'Star', 'musician', '9000')
print(wrk1._income)
print(wrk2._income)

# print(wrk1.name, wrk1.surname, wrk1.position, wrk1._income['wage'])
print(wrk1.get_full_name())
print(wrk1.get_total_income(500))

# print(wrk2.name, wrk2.surname, wrk2.position, wrk2._income['wage'])
print(wrk2.get_full_name())
print(wrk2.get_total_income(250))
