# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное
# сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self, title='Ручка'):
        super().__init__()
        self.title = title

    def draw(self):
        print(f'{self.title} начала рисовать')


class Handle(Stationery):
    def __init__(self, title="Маркер"):
        super().__init__()
        self.title = title

    def draw(self):
        print(f'{self.title} начала рисовать')


class Pencil(Stationery):
    def __init__(self, title="Карандаш"):
        super().__init__()
        self.title = title

    def draw(self):
        print(f'{self.title} начала рисовать')


pen1 = Pen()
pen1.draw()
pencil1 = Pencil()
pencil1.draw()
handle1 = Handle()
handle1.draw()
stationery1 = Stationery()
stationery1.draw()
