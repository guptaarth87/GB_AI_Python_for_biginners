"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
 — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
 и завершать скрипт.
"""

from time import sleep


class TrafficLight:
    __color = ''
    TL_status = 'выключен'

    def __init__(self):
        print('Запуск.')
        print(
            f'Текущий режим светофора:{self.TL_status}.\n Корректное переключение:красный, желтый, зеленый.\n'
            f'--------------------------------------------')


    def _sleep_print(self,slp):
        for i in range(slp):
            print(slp-i)
            sleep(1)


    def _tl_change(self, stat, slp=10):

        self.status = stat
        print(f'Светофор переключен в режим {self.status}')
        self._sleep_print(slp)

        if self.status == 'красный':
            new_color = 'желтый'
        elif self.status == 'желтый':
            new_color = 'зеленый'
        else:
            new_color = 'красный'

        return new_color

    def running(self, new_color):
        self.__color = new_color
        running_result=True
        if self.__color == 'красный' and (self.TL_status == 'зеленый' or self.TL_status == 'выключен'):
            print(f'Светофор готов к переключению в следующий режим: {self._tl_change(self.__color,7)}.')
            self.TL_status=self.__color

        elif self.__color=='желтый' and self.TL_status=='красный':
            print(f'Светофор готов к переключению в следующий режим: {self._tl_change(self.__color,2)}.')
            self.TL_status = self.__color
        elif self.__color=='зеленый' and self.TL_status=='желтый':
            print(f'Светофор готов к переключению в следующий режим: {self._tl_change(self.__color)}.')
            self.TL_status = self.__color
        else:
            print(
                f'Корректное переключение (ввод):красный, желтый, зеленый.\n'
                f' Вы ввели: {self.__color}.\n')
            running_result=False
        print(f'Текущий режим светофора:{self.TL_status}.')
        return running_result

tl = TrafficLight()
while tl.running(input('Задайте цвет сигнала светофора:')):
    pass

