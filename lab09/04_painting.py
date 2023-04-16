#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать (или при необходимости написать) функции отрисовки
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)



# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
import simple_draw as sd
from drawing import rainbow as rb, house as H, tree, sun


sd.resolution = (1920, 1080)

sd.ellipse(sd.Point(-180, -250), sd.Point(2100, 250), color=sd.COLOR_GREEN)

rainbow_start = sd.Point(760, -150)
rainbow_rad = 1300
rainbow_width = 15
rb.draw_rainbow(rainbow_start, rainbow_rad, rainbow_width)

house_height = 400
house_width = 400
house_start = 560
house_lines_color = sd.COLOR_WHITE
house_color = (136,69,53)
H.draw_house(house_height+150, house_width, house_start, house_lines_color, house_color)

sun_start = sd.Point(300, 900)
sun_radius = 80
sun.drawing_sun(sun_start, sun_radius)

tree_leaves_color = sd.COLOR_GREEN
tree_color = (101, 67, 33)
tree_start = sd.Point(1400, 150)
tree.draw_tree(tree_start, tree_leaves_color, tree_color)
sd.pause()