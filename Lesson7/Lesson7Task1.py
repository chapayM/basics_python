# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.
class Matrix:
    def __init__(self, numbers_list):
        self.numbers_list = numbers_list

    def __str__(self):
        matrix_view = ''
        for el in self.numbers_list:
            s = '|'
            for i in el:
                s += f'{i} '
            matrix_view += f'{s}|\n'
        return f"Матрица: \n{matrix_view}"

    def __add__(self, other):
        if len(self.numbers_list) != len(other.numbers_list) or len(self.numbers_list[0]) != len(other.numbers_list[0]):
            return f'Сложение матриц не возможно из-за разных размерностей'
        else:
            row = 0
            new_matrix = []
            for str1 in self.numbers_list:
                collum = 0
                new_row_list = []
                for el1 in str1:
                    new_el = self.numbers_list[row][collum] + other.numbers_list[row][collum]
                    new_row_list.append(new_el)
                    collum += 1
                new_matrix.append(new_row_list)
                row += 1
            return Matrix(new_matrix)


numbers_1 = Matrix([[1, 2, 3], [4, 5, 6]])
print(numbers_1)
numbers_2 = Matrix([[31, 32], [37, 43]])
print(numbers_2)
numbers_3 = Matrix([[1, 2, 3], [4, 5, 6]])
print(numbers_1 + numbers_3)
print(numbers_1 + numbers_2)
