#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.

start_x = 50
end_x = 350
for i in range(len(rainbow_colors)):
    start_x =+ 5
    end_x += 5
    sd.line(start_point = sd.Point(start_x, 50), end_point = sd.Point(end_x, 450) , color = rainbow_colors[i], width = 4)
    

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()
