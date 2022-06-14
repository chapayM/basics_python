# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
class Storage:
    def __init__(self, *office_equipment):  # сколько у него мест хранения, какая техника на складе
        self.name = input('Введите наименование склада: ')
        self.volume = None
        while self.volume is None:
            self.volume = type_err(input('Введите количества мест хранения на складе: '), 1)
        self.office_equipment = list(office_equipment)
        self.total = len(self.office_equipment)

    def __str__(self):
        return f'{self.name}, {self.volume}, {self.total}, {self.office_equipment}'


class OfficeEquipment:
    def __init__(self, type_eq, storage=None, storage_place=None, department=None, used=False,
                 on_storage=False):

        self.brand = input("Введите марку: ")
        self.model = input("Введите модель: ")
        self.type_eq = type_eq
        self.storage = storage
        self.storage_place = storage_place
        self.department = department
        self.used = used
        self.on_storage = on_storage

    def __str__(self):
        if self.on_storage == True:
            return f'{self.type_eq}, {self.brand}, {self.model}, на скаладе, б/у {self.used}'
        else:
            return f'{self.type_eq}, {self.brand}, {self.model}, в подразделение - {self.department}, б/у {self.used}'

    def acceptance_of_equipment(self, storage, storage_place):
        storage.total += 1
        if storage.total <= storage.volume:
            self.on_storage = True
            self.storage = storage
            self.storage_place = storage_place
            storage.office_equipment.append(self)
        else:
            storage.total = storage.total - 1
            print(f'Склад {storage.name} полностью заполнен, размещение оборудования не возможно')

    def equipment_to_department(self, department, storage):
        self.on_storage = False
        self.department = department
        self.used = True
        self.storage_place = None
        storage.total = storage.total - 1
        storage.office_equipment.remove(self)


class Printer(OfficeEquipment):
    def __init__(self, color=False, type_eq="Принтер", storage=None, storage_place=None,
                 department=None, used=False, on_storage=False):
        super().__init__(storage, storage_place, department, used, on_storage)
        self.printing_speed = None
        while self.printing_speed is None:
            self.printing_speed = type_err(input('Введите скорость печати: '), 1)
        self.color = None
        while self.color is None:
            self.color = type_err(input('Принтер цветной да/нет?: '), 3)
        self.type_eq = type_eq


class Scanner(OfficeEquipment):

    def __init__(self, mobile=False, type_eq="Сканнер", storage=None, storage_place=None,
                 department=None, used=False, on_storage=False):
        super().__init__(storage, storage_place, department, used, on_storage)
        self.resolution = None
        while self.resolution is None:
            self.resolution = type_err(input('Введите разрешение сканнера: '), 1)
        self.mobile = None
        while self.mobile is None:
            self.mobile = type_err(input("Сканнер мобильный да/нет? "), 3)
        self.type_eq = type_eq


class Copier(OfficeEquipment):

    def __init__(self, color=False, type_eq="Сканнер", storage=None, storage_place=None,
                 department=None, used=False, on_storage=False):
        super().__init__(storage, storage_place, department, used, on_storage)
        self.resolution = None
        while self.resolution is None:
            self.resolution = type_err(input('Введите разрешение копира: '), 1)
        self.color = None
        while self.color is None:
            self.color = type_err(input('Копир цветной да/нет?: '), 3)
        self.type_eq = type_eq


def type_err(date, type_error):
    if type_error == 1:  # Проверка на целое число
        try:
            return int(date)
        except ValueError:
            print("Данное значение должно быть числом")
            return None
    elif type_error == 2:  # проверка на тип оборудования
        if date in ['Принтер', "принтер"]:
            return "Принтер"
        elif date in ['Сканнер', "сканнер"]:
            return "Сканнер"
        elif date in ['Копир', "копир"]:
            return "Копир"
        else:
            print("Данный тип оборудования не поддерживается")
            return None
    elif type_error == 3:  # Проверка на да/нет
        if date in ['Нет', "нет", "No", "no"]:
            return False
        elif date in ['Yes', "yes", "Да", "да"]:
            return True
        else:
            print("Данный тип оборудования не поддерживается")
            return None


storage1 = Storage()
office_eq = []
for i in range(1, storage1.volume + 1):
    class_eq = None
    while class_eq is None:
        class_eq = type_err(input("Введите тип передаваемой на склад техники - принтер/сканнер/копир: "), 2)
    if class_eq == "Принтер":
        office_eq.append(Printer())
    elif class_eq == "Сканнер":
        office_eq.append(Scanner())
    elif class_eq == "Копир":
        office_eq.append(Copier())
    office_eq[i - 1].acceptance_of_equipment(storage1, i)
office_eq.append(Printer())
office_eq[3].acceptance_of_equipment(storage1, 3)
print(storage1)
print(office_eq[0])
office_eq[0].equipment_to_department(input("Введите наименование подразделения: "), storage1)
print(storage1)
print(office_eq[0])
