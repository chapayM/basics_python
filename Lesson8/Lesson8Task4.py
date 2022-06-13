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
    def __init__(self, name, volume=10, total=0,
                 *office_equipment):  # сколько у него мест хранения, какая техника на складе
        self.name = name
        self.volume = volume
        self.office_equipment = list(office_equipment)
        self.total = total

    def __str__(self):
        return f'{self.name}, {self.volume}, {self.total}, {self.office_equipment}'


class OfficeEquipment:
    def __init__(self, brand, model, type_eq, storage=None, storage_place=None, department=None, used=False,
                 on_storage=False):

        self.brand = brand
        self.model = model
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
    def __init__(self, brand, model, printing_speed, color=False, type_eq="Принтер", storage=None, storage_place=None,
                 department=None, used=False, on_storage=False):
        super().__init__(brand, model, storage, storage_place, department, used, on_storage)
        self.printing_speed = printing_speed
        self.color = color
        self.type_eq = type_eq


class Scanner(OfficeEquipment):

    def __init__(self, brand, model, resolution, mobile=False, type_eq="Сканнер", storage=None, storage_place=None,
                 department=None, used=False, on_storage=False):
        super().__init__(brand, model, storage, storage_place, department, used, on_storage)
        self.resolution = resolution
        self.mobile = mobile
        self.type_eq = type_eq


class Copier(OfficeEquipment):

    def __init__(self, brand, model, resolution, color=False, type_eq="Сканнер", storage=None, storage_place=None,
                 department=None, used=False, on_storage=False):
        super().__init__(brand, model, storage, storage_place, department, used, on_storage)
        self.resolution = resolution
        self.color = color
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


storage1 = Storage("Склад на Зоологической", 5)
printer1 = Printer(brand='Samsung', model='SCX-443', storage_place=None, department=None, used=False, on_storage=False,
                   printing_speed=100, color=False)
printer2 = Printer('Samsung', 'SCX-480', 1000, True)
printer3 = Printer('Samsung', 'SCX-444', 100)
scanner1 = Scanner("Toshiba", 'RD-554', 1000, False)
copier1 = Copier(brand='Xerox', model='1445VN', storage_place=None, department=None, used=False, on_storage=False,
                 storage=None, resolution=3000, color=False)
copier2 = Copier('Canon', 'CDS345N', 350)
offequlist = [scanner1, printer1, printer2, printer3, copier1]
i = 1
for el in offequlist:
    el.acceptance_of_equipment(storage1, i)
    print(storage1)
    print(el)
    i += 1
copier2.acceptance_of_equipment(storage1, 6)
print(storage1)
copier1.equipment_to_department('Бухгалтерия', storage1)
print(storage1)
print(copier1)

class_eq = None
while class_eq is None:
    class_eq = type_err(input("Введите тип передаваемой на склад техники - принктер/сканнер/копир: "), 2)
name_eq = input("Введите марку передаваемой на склад техники: ")
model_eq = input("Введите модель передаваемой на склад техники: ")
if class_eq == "Принтер":
    printing_speed_eq = None
    color_eq = None
    while printing_speed_eq is None:
        printing_speed_eq = type_err(input("Введите скорость печати: "), 1)
    while color_eq is None:
        color_eq = type_err(input("Принтер цветной (да/нет)?: "), 3)
    printer4 = Printer(brand=name_eq, model=model_eq, printing_speed=printing_speed_eq, color=color_eq)
elif class_eq == "Копир":
    resolution_eq = None
    color_eq = None
    while resolution_eq is None:
        resolution_eq = type_err(input("Введите разрешение: "), 1)
    while color_eq is None:
        color_eq = type_err(input("Принтер цветной (да/нет)?: "), 3)
    copier3 = Copier(brand=name_eq, model=model_eq, resolution=resolution_eq, color=color_eq)
elif class_eq == "Сканер":
    resolution_eq = None
    mobile_eq = None
    while resolution_eq is None:
        resolution_eq = type_err(input("Введите разрешение: "), 1)
    while mobile_eq is None:
        mobile_eq = type_err(input("Мобильный сканнер (да/нет)?: "), 3)
    scanner2 = Scanner(brand=name_eq, model=model_eq, resolution=resolution_eq, mobile=mobile_eq)
