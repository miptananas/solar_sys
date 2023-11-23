# coding: utf-8
# license: GPLv3

import pygame as pg
import pygame_widgets
from solar_world import World
from solar_vis import calculate_scale_factor, Drawer, Menu
from solar_model import recalculate_space_objects_positions
from solar_input import read_space_objects_data_from_yaml, write_space_objects_data_to_yaml
from solar_stats import check_system, calculate_speed, calculate_distance, show_graph
import time
import numpy as np


def execution(delta, world: World) -> None:
    """Функция исполнения -- выполняется циклически, вызывая обработку всех небесных тел,
    а также обновляя их положение на экране.
    Цикличность выполнения зависит от значения переменной perform_execution в объекте типа World.
    При perform_execution == True функция запрашивает вызов самой себя по таймеру через от 1 мс до 100 мс.
    """
    recalculate_space_objects_positions(world.space_objects, world.scale_factor, delta)
    world.model_time += delta
    if check_system(world.space_objects):
        world.graph_time = np.append(world.graph_time, world.model_time)
        world.graph_speed = np.append(world.graph_speed, calculate_speed(world.space_objects))
        world.graph_S = np.append(world.graph_S, calculate_distance(world.space_objects))


def start_execution(world: World) -> None:
    """Обработчик события нажатия на кнопку Start.
    Запускает циклическое исполнение функции execution.
    """
    world.perform_execution = True


def pause_execution(world: World) -> None:
    """
    Останавливает выполнение программы
    """
    world.perform_execution = False


def stop_execution(world: World) -> None:
    """Обработчик события нажатия на кнопку Start.
    Останавливает циклическое исполнение функции execution.
    """
    world.alive = False


def open_file(world: World) -> None:
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в список space_objects в объекте типа World
    """
    in_filename = "./configs/systems/yaml/one_satellite.yaml"
    world.space_objects = read_space_objects_data_from_yaml(in_filename)
    world.drawable_objects = world.space_objects
    max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in world.space_objects])
    world.scale_factor = calculate_scale_factor(max_distance)


def handle_events(events, world: World) -> None:
    """
    Обрабатывает действия пользователя и вызывает реакцию интерфейса и всей программы на них
    """
    for event in events:
        if event.type == pg.QUIT:
            world.alive = False
    pygame_widgets.update(events)


def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """
    print("Modelling started!")

    pg.init()

    width = 900
    height = 750
    screen = pg.display.set_mode((width, height))
    world = World()
    menu = Menu(
        screen,
        pause_callback=lambda: pause_execution(world),
        stop_callback=lambda: stop_execution(world),
        play_callback=lambda: start_execution(world),
        load_callback=lambda: open_file(world),
    )
    drawer = Drawer(screen, menu)
    world.perform_execution = True

    while world.alive:
        execution(10000, world)
        drawer.update(world.drawable_objects)
        handle_events(pg.event.get(), world)
        drawer.display_update()
        time.sleep(1.0 / 10)

    write_space_objects_data_to_yaml("output.txt", world.space_objects)
    if check_system(world.space_objects):
        show_graph(world.graph_time, world.graph_speed, world.graph_S)

    print("Modelling finished!")


if __name__ == "__main__":
    main()
