# coding: utf-8
# license: GPLv3

import pygame as pg
import pygame.draw
import pygame.locals

from pygame_widgets.slider import Slider
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
from typing import Callable

from solar_objects import SpaceObject
from typing import Tuple


"""Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие гaрафические объекты и перемещающие их на экране, принимают физические координаты
"""

header_font = "Arial-16"
"""Шрифт в заголовке"""

window_width = 900
"""Ширина окна"""

window_height = 750
"""Высота окна"""

scale_factor = 1
"""Масштабирование экранных координат по отношению к физическим.

Тип: float

Мера: количество пикселей на один метр."""


def calculate_scale_factor(max_distance):
    """Вычисляет значение глобальной переменной **scale_factor** по данной характерной длине"""
    # FIXME
    global scale_factor
    scale_factor = 0.4 * min(window_height, window_width) / max_distance
    print("Scale factor:", scale_factor)
    return scale_factor


def scale_x(x):
    """Возвращает экранную **x** координату по **x** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **x** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.

    Параметры:

    **x** — x-координата модели.
    """

    return int(x * scale_factor) + window_width // 2


def scale_y(y):
    """
    Возвращает экранную **y** координату по **y** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **y** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.
    Направление оси развёрнуто, чтобы у модели ось **y** смотрела вверх.

    Параметры:

    **y** — y-координата модели.
    """
    return -int(y * scale_factor) + window_height // 2


class Drawer:
    def __init__(self, screen, menu):
        self.screen = screen
        self.menu = menu

    def update(self, figures):
        self.screen.fill((0, 0, 0))
        for figure in figures:
            figure.draw(self.screen)
        self.menu.draw()

    @staticmethod
    def display_update() -> None:
        pg.display.update()


class DrawableObject:
    """
    Класс, присвайвающий объектам функцию отрисовки.
    """

    def __init__(self, obj):
        self.obj: SpaceObject = obj

    def draw(self, surface):
        """
        Отрисовывает объекты на экране.

        Параметры:

        **surface** - pg.display.set_mode((width, height))
        """

        if self.obj.alive:
            x = int(scale_x(self.obj.x))
            y = int(scale_y(self.obj.y))
            pygame.draw.circle(surface, self.obj.color, (x, y), self.obj.R)


class Menu:
    """
    Класс отрисовки меню
    Каждая кнопку можно связать с действием через button_callback
    В button_callback можно передать аргументы, если это нужно [Документация](https://pygamewidgets.readthedocs.io/en/stable/widgets/button/)
    Объявление button_callback находится в solar_main
    Стоит ли их перенести в данный класс?
    """

    def __init__(
        self,
        screen: pg.Surface,
        pause_callback: Callable = lambda: print("Pause"),
        stop_callback: Callable = lambda: print("Stop"),
        play_callback: Callable = lambda: print("Play"),
        load_callback: Callable = lambda: print("Load"),
        submit_box_callback: Callable = lambda: print("Submit Box"),
    ):
        self.screen = screen
        self.button_pause = self._create_button(
            10, 10, text="Pause", on_click=pause_callback,
        )
        self.button_stop = self._create_button(
            10, 40, text="Stop", on_click=stop_callback,
        )
        self.button_play = self._create_button(
            115, 10, text="Play", on_click=play_callback,
        )
        self.button_load = self._create_button(
            115, 40, text="Load", on_click=load_callback,
        )
        self.submit_box = self._create_submit_box(
            25, 70, on_submit=submit_box_callback,
        )
        self.value_box = self._create_text_box(
            60, 150,
        )
        self.slider = self._create_slider(
            25, 110,
        )

    def draw(self) -> None:
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, 200, 180))
        self.value_box.setText(f"speed: {self.get_slider_value()}")

    def get_slider_value(self) -> float:
        return self.slider.getValue()

    def _create_button(
        self,
        x_pos: int,
        y_pos: int,
        width: int = 75,
        height: int = 25,
        text: str = "Hello",
        font_size: int = 25,
        margin: int = 20,
        inactive_color: Tuple[int, int, int] = (200, 50, 0),
        hover_color=(150, 0, 0),
        pressed_color=(0, 200, 20),
        radius: int = 20,
        on_click: Callable = lambda: print("Click"),
    ) -> Button:
        return Button(
            win=self.screen,
            x=x_pos,
            y=y_pos,
            width=width,
            height=height,
            text=text,
            fontSize=font_size,
            margin=margin,
            inactiveColour=inactive_color,
            hoverColour=hover_color,
            pressedColour=pressed_color,
            radius=radius,
            onClick=on_click,
        )

    def _create_slider(
        self,
        x_pos: int,
        y_pos: int,
        width: int = 150,
        height: int = 25,
        min: int = 1,
        max: int = 100,
        step: int = 1,
    ) -> Slider:
        return Slider(
            win=self.screen,
            x=x_pos,
            y=y_pos,
            width=width,
            height=height,
            min=min,
            max=max,
            step=step,
        )

    def _create_submit_box(
        self,
        x_pos: int,
        y_pos: int,
        width: int = 150,
        height: int = 25,
        is_sub_widget: bool = False,
        on_submit: Callable = lambda: print("Submit"),
    ) -> TextBox:
        return TextBox(
            win=self.screen,
            x=x_pos,
            y=y_pos,
            width=width,
            height=height,
            isSubWidget=is_sub_widget,
            onSubmit=on_submit,
        )

    def _create_text_box(
        self,
        x_pos: int,
        y_pos: int,
        width: int = 80,
        height: int = 25,
    ) -> TextBox:
        return TextBox(
            win=self.screen,
            x=x_pos,
            y=y_pos,
            width=width,
            height=height,
        )


if __name__ == "__main__":
    print("This module is not for direct call!")
