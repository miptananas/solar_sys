# coding: utf-8
# license: GPLv3


class SpaceObject:
    """Тип данных, описывающий объект.
    Содержит массу, координаты, скорость объекта,
    а также визуальный радиус объекта в пикселах и её цвет.
    """

    def __init__(self, type: str, R: float, color: str, m: float, x: float, y: float, v_x: float, v_y: float):
        self.type = type  # Признак объекта star или planet
        self.m = m  # Масса объекта
        self.x = x  # Координата по оси **x**
        self.y = y  # Координата по оси **y**
        self.Vx = v_x  # Скорость по оси **x**
        self.Vy = v_y  # Скорость по оси **y**
        self.Fx = 0  # Сила по оси **x**
        self.Fy = 0  # Сила по оси **y**
        self.R = R  # Радиус объекта
        self.color = color  # Цвет объекта
        self.alive = 1  # Существование объекта


if __name__ == "__main__":
    print("This module is not for direct call!")
