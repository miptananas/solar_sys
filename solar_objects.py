# coding: utf-8
# license: GPLv3


class SpaceObject:
    """Тип данных, описывающий объект.
    Содержит массу, координаты, скорость объекта,
    а также визуальный радиус объекта в пикселах и её цвет.
    """

    # TODO: Дополнить документацию
    # TODO: Добавить возможность инициализации параметров через __init__

    def __init__(self, type):
        self.type = type  # Признак объекта star или planet
        self.m = 1  # Масса объекта
        self.x = 0  # Координата по оси **x**
        self.y = 0  # Координата по оси **y**
        self.Vx = 0  # Скорость по оси **x**
        self.Vy = 0  # Скорость по оси **y**
        self.Fx = 0  # Сила по оси **x**
        self.Fy = 0  # Сила по оси **y**
        self.R = 5  # Радиус объекта
        self.color = "red"  # Цвет объекта
        self.alive = 1  # Существование объекта


if __name__ == "__main__":
    print("This module is not for direct call!")
