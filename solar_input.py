# coding: utf-8
# license: GPLv3

import yaml
from typing import List
from solar_objects import SpaceObject
from solar_vis import DrawableObject


def read_space_objects_data_from_yaml(input_filename) -> List[SpaceObject]:
    """Функция считывает словарь параметров из файла и передает из в объект"""
    # SpaceObject(**config)
    # TODO: Дополнить созданием объектов типов Зведа/Планета
    with open(input_filename, "r") as input_file:
        configs = yaml.safe_load(input_file)
    # FIXME
    return []


def write_space_objects_data_to_yaml(output_filename, space_objects: List[SpaceObject]) -> None:
    """Функция преобразует объекты в список словарей и записывает в файл"""
    # TODO: Проверить корректность работы функции
    with open(output_filename, "w") as output_file:
        yaml.safe_dump(space_objects, output_file)
    # FIXME


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    DEPRECATED
    """
    # TODO: Убрать из релиза

    objects = []
    with open(input_filename, "r") as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == "#":
                continue  # пустые строки и строки-комментарии пропускаем

            object_type = line.split()[0].lower()
            if object_type == "star":
                star = SpaceObject("star")
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = SpaceObject("planet")
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return [DrawableObject(obj) for obj in objects]


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.

    Входная строка должна иметь слеюущий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.

    Пример строки:

    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описанием звезды.

    **star** — объект звезды.
    DEPRECATED
    """
    # TODO: Убрать из релиза
    star_parameters = line.split()
    star.R = float(star_parameters[1])
    star.color = star_parameters[2]
    star.m = float(star_parameters[3])
    star.x = float(star_parameters[4])
    star.y = float(star_parameters[5])
    star.Vx = float(star_parameters[6])
    star.Vy = float(star_parameters[7])


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Входная строка должна иметь слеюущий формат:

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.

    Пример строки:

    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.

    **planet** — объект планеты.
    DEPRECATED
    """
    planet_parameters = line.split()
    planet.R = float(planet_parameters[1])
    planet.color = planet_parameters[2]
    planet.m = float(planet_parameters[3])
    planet.x = float(planet_parameters[4])
    planet.y = float(planet_parameters[5])
    planet.Vx = float(planet_parameters[6])
    planet.Vy = float(planet_parameters[7])


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.

    Строки должны иметь следующий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла

    **space_objects** — список объектов планет и звёзд
    DEPRECATED
    """
    # TODO: Убрать из релиза
    with open(output_filename, "w") as out_file:
        for obj in space_objects:
            if obj.obj.alive == 0:
                continue
            out_file.write(
                str(obj.obj.type)
                + " "
                + str(obj.obj.R)
                + " "
                + str(obj.obj.color)
                + " "
                + str(obj.obj.m)
                + " "
                + str(obj.obj.x)
                + " "
                + str(obj.obj.y)
                + " "
                + str(obj.obj.Vx)
                + " "
                + str(obj.obj.Vy)
                + "\n"
            )


if __name__ == "__main__":
    print("This module is not for direct call!")
