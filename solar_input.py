# coding: utf-8
# license: GPLv3

import yaml
from typing import List
from solar_objects import SpaceObject
from solar_vis import DrawableObject


def read_space_objects_data_from_yaml(input_filename) -> List[SpaceObject]:
    """Функция считывает словарь параметров из файла и передает из в объект"""
    with open(input_filename, "r") as input_file:
        configs = yaml.safe_load(input_file)

    configs_float = []
    for config in configs:
        configs_float.append({})
        for t in config:
            if t not in ['type', 'color']:
                configs_float[-1][t] = float(config[t])
            else:
                configs_float[-1][t] = config[t]
    return [SpaceObject(**cfg) for cfg in configs_float]


def write_space_objects_data_to_yaml(output_filename, space_objects: List[SpaceObject]) -> None:
    """Функция преобразует объекты в список словарей и записывает в файл"""
    with open(output_filename, "w") as output_file:
        yaml.safe_dump([{'type': obj.type,
                         'R': obj.R,
                         'color': obj.color,
                         'm': obj.m,
                         'x': obj.x,
                         'y': obj.y,
                         'v_x': obj.Vx,
                         'v_y': obj.Vy} for obj in space_objects], output_file)


if __name__ == "__main__":
    print("This module is not for direct call!")
