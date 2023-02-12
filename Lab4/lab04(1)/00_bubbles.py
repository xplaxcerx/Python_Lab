#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код    
point = sd.get_point(500, 350)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius)
sd.pause()

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
# TODO здесь ваш код
def buble_ok(point, step, color):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color)

color = 215
point = sd.get_point(500, 350)
buble_ok(point, 10, color)
sd.pause()

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
for x in range(170, 1000, 100):
    point = sd.get_point(x, 350)
    sd.circle(center_position=point)
sd.pause()

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
for x in range(170, 1100, 100):
    for y in range(100, 400, 100):
       sd.circle(center_position=point)

sd.pause()
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
import random
for i in range(100):
    point = sd.random_point()
    color = sd.random_color()
    step = random.randint(10, 50)
    sd.circle(center_position=point, radius = step, color = color)
sd.pause()
