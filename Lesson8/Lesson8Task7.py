# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
# (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class Complex_num():
    def __init__(self, real_part, complex_part):
        self.real_part = real_part
        self.complex_part = complex_part

    # def __str__(self):
    #     if self.real_part == 0:
    #         return f'{self.complex_part}i'
    #     elif self.complex_part == 0:
    #         return f'{self.real_part}'
    #     else:
    #         return f'{self.real_part} + {self.complex_part}i'

    def __add__(self, other):
        real_part = self.real_part + other.real_part
        complex_part = self.complex_part + other.complex_part
        return real_part, complex_part

    def __mul__(self, other):
        real_part = self.real_part*other.real_part-self.complex_part*other.complex_part
        complex_part = self.real_part*other.complex_part+self.complex_part*other.real_part
        return real_part, complex_part


com1 = Complex_num(1, -1)
com2 = Complex_num(2, 2)
com3 = com1 + com2
print(com3)
com4 = com1 * com2
print(com4)