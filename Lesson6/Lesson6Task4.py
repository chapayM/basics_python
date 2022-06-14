# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.
class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed = int(input('Введите скорость: '))
        print('Машина поехала')
        return self.speed

    def stop(self):
        print('Машина остановилась')
        self.speed = 0
        return self.speed

    def turn(self):
        direction = input('Введите куда повернула машина (налево/направо): ')
        print(f'Мaшина {self.name} повернула {direction}')
        return direction

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed}')
        if type(self) == TownCar and self.speed > 60:
            print('Внимание! Скорость превышена!')
        elif type(self) == WorkCar and self.speed > 40:
            print('Внимание! Скорость превышена!')
        elif self.speed > 60:
            print(f'Это {self.car_type}. Это нормальная скорость.')


class TownCar(Car):

    def __init__(self, speed, color, name, car_type, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.car_type = car_type


class WorkCar(Car):

    def __init__(self, speed, color, name, car_type, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.car_type = car_type


class SportCar(Car):

    def __init__(self, speed, color, name, car_type, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.car_type = car_type


class PoliceCar(Car):

    def __init__(self, speed, color, name, car_type, is_police=True):
        super().__init__(speed, color, name, is_police)
        self.car_type = car_type


towncar1 = TownCar(50, 'black', 'Ford', 'Обычная машина')
print(towncar1.car_type)
towncar1.go()
towncar1.show_speed()
towncar1.turn()
towncar1.stop()
towncar1.show_speed()
policecar1 = PoliceCar(100, 'white', 'VAZ', 'Полиция')
policecar1.show_speed()
print(policecar1.color)
