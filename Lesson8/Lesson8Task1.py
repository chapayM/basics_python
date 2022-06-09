# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных
class Date:

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def date_str_num(cls, date_str):
        try:
            month = int(date_str.split('-')[1])
            a = cls.check_month(month)
        except ValueError:
            print('Запись даты не в формате ДД-ММ-ГГГГ')
            return None
        try:
            year = int(date_str.split('-')[2])
            b = cls.check_year(year)
        except ValueError:
            print('Запись даты не в формате ДД-ММ-ГГГГ')
            return None
        try:
            day = int(date_str.split('-')[0])
            c = cls.check_day(day, month, year)
        except ValueError:
            print('Запись даты не в формате ДД-ММ-ГГГГ')
            return None
        if a and b and c is True:
            date_list = [day, month, year]
            return date_list
        else:
            return None

    @staticmethod
    def check_month(month):
        if 1 <= month <= 12:
            return True
        else:
            print('Ошибка в написание месяца.')

    @staticmethod
    def check_year(year):
        if 1900 <= year <= 2004:
            return True
        elif year > 2004:
            print('Наш сервис доступен только для лиц старше 18 лет.')
        else:
            print('Мы не уверены, что вы верно ввели год рождения, напишите нам в техподдержку если вы не ошиблись')

    @staticmethod
    def check_day(day, month, year):
        if month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:
            return True
        elif month in [4, 6, 9, 11] and day <= 30:
            return True
        elif month == 2 and year in [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952,
                                     1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004] \
                and day <= 29:
            return True
        elif month == 2 and year not in [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952,
                                         1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004] \
                and day <= 28:
            return True
        else:
            print('Ошибка в написание дня.')


# print(Date.date_str_num("11-12-1981"))
# print(Date.date_str_num("11-12-1881"))
# print(Date.date_str_num("11-13-1881"))
print(Date.date_str_num("1d-0d-200s"))
# print(Date.date_str_num("11-17-2007"))
# print(Date.date_str_num("17-0d-200s"))
# print(Date.date_str_num("11-01-2007"))
# print(Date.date_str_num("56-01-2007"))
print(Date.date_str_num("29-02-1899"))

