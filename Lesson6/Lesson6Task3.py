# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом
# премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить
# значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, name=0, surname=0, position=0, wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"Wage": wage, "Bonus": bonus}


class Position(Worker):


    def get_full_name(self):
        self.name = input("Введите имя сотрудника: ")
        self.surname = input('Введите фамилию сотрудника: ')
        return print(f'{self.name} {self.surname}')

    def get_total_income(self):
        self.wage = float(input('Введите оклад: '))
        self.bonus = float(input('Введите премию: '))
        self._income = {"wage": self.wage, "bonus": self.bonus}
        return self._income


pos1 = Position()
pos1.get_full_name()
pos1.get_total_income()
print(pos1.name)
print(pos1.surname)
print(pos1._income)
pos2 = Position()
pos2.get_full_name()
pos2.get_total_income()
print(pos2.name)
print(pos2.surname)
print(pos2._income)
# woker1 = Worker()
# print(woker1.surname)
