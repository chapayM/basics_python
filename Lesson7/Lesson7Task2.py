# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import abstractmethod


class Clothes():
    size = 0

    def __init__(self, size):
        Clothes.size += size
        self.total_size = Clothes.size

    @abstractmethod
    def fabric_size(self):
        pass


class Coat(Clothes):
    total_size = 0

    def __init__(self, v):
        self.v = v
        self.size = v / 6.5 + 0.5
        Clothes.__init__(self, self.size)

    def fabric_size(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    total_size = 0

    def __init__(self, h):
        self.h = h
        self.size = h * 2 + 0.3
        Clothes.__init__(self, self.size)

    @property
    def fabric_size(self):
        return self.h * 2 + 0.3


coat_1 = Coat(52)
suit_1 = Suit(1.7)
suit_2 = Suit(5)
print(coat_1.fabric_size())
print(suit_1.fabric_size)
print(suit_2.size)
print(coat_1.total_size)
print(suit_2.total_size)
