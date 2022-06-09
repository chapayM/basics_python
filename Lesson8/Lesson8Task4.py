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
    def __init__(self, type_office_equipment, value, volume=10, *office_equipment):#сколько у него мест хранения, какая техника на складе
        self.type_office_equipment = type_office_equipment
        self.value = value
        self.volume = volume
        self.office_equipment = office_equipment


class OfficeEquipment:
    def __init__(self, brand, model, storage_place=None, department=None, used=False, on_storage=False):
        self.brand = brand
        self.model = model
        self.storage_place = storage_place
        self.department = department
        self.used = used
        self.on_storage = on_storage


class Printer(OfficeEquipment):
    def __init__(self, printing_speed, brand, model, storage_place, department, used, on_storage, color=False):
        super().__init__(brand, model, storage_place, department, used, on_storage)
        self.printing_speed = printing_speed
        self.color = color

class Scanner(OfficeEquipment):
    def _init__(self, resolution, brand, model, storage_place, department, used, on_storage, mobile=False):
        super().__init__(brand, model, storage_place, department, used, on_storage)
        self.resolution = resolution
        self.mobile = mobile


class Copier(OfficeEquipment):
    def _init__(self, resolution, brand, model, storage_place, department, used, on_storage, color=False):
        super().__init__(brand, model, storage_place, department, used, on_storage)
        self.resolution = resolution
        self.color = color
