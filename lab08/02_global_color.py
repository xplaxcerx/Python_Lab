# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр 01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см /results/exercise_02_global_color.jpg

# TODO здесь ваш код
#choice_color = 
list_of_colors = {1: sd.COLOR_RED, 2: sd.COLOR_ORANGE, 3: sd.COLOR_YELLOW, 4: sd.COLOR_GREEN, 
5: sd.COLOR_CYAN, 6: sd.COLOR_BLUE, 7: sd.COLOR_PURPLE}

list_of_choice = {1: '1 - красный', 2: '2 - оранжевый', 3: '3 - желтый', 4: '4 - зеленый', 
5: '5 - голубой', 6: '6 - синий', 7: '7 - фиолетовый'}

for color in list_of_choice.values():
    print(color)
a = int(input('номер выбранного цвета: '))

if a in list_of_colors:
    sp_triangle = sd.Point(100, 250)
    for i in range(30, 360, 120):
        gsp_triangle = sd.get_vector(sp_triangle, angle = i, length = 50, width = 3)
        gsp_triangle.draw(list_of_colors[a])
        sp_triangle = gsp_triangle.end_point
if a in list_of_colors:    
    sp_square = sd.Point(200, 250)
    for i in range(30, 360, 90):
        gsp_square = sd.get_vector(sp_square, angle = i, length = 50, width = 3)
        gsp_square.draw(list_of_colors[a])
        sp_square = gsp_square.end_point
if a in list_of_colors:
    sp_pentagon = sd.Point(300, 250)
    for i in range(30, 360, 72):
        gsp_pentagon = sd.get_vector(sp_pentagon, angle = i, length = 50, width = 3)
        gsp_pentagon.draw(list_of_colors[a])
        sp_pentagon = gsp_pentagon.end_point
if a in list_of_colors:
    sp_hexagon = sd.Point(400, 250)
    for i in range(30, 360, 60):
        gsp_hexagon = sd.get_vector(sp_hexagon, angle = i, length = 50, width = 3)
        gsp_hexagon.draw(list_of_colors[a])
        sp_hexagon = gsp_hexagon.end_point
sd.pause()

