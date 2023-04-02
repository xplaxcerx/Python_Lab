# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр 02_global_color.py скопировать сюда
# Результат решения см results/exercise_03_shape_select.jpg

# TODO здесь ваш код
list_of_colors = {1: sd.COLOR_RED, 2: sd.COLOR_ORANGE, 3: sd.COLOR_YELLOW, 4: sd.COLOR_GREEN, 
5: sd.COLOR_CYAN, 6: sd.COLOR_BLUE, 7: sd.COLOR_PURPLE}

list_of_choice = {1: '1 - Красный', 2: '2 - Оранжевый', 3: '3 - Желтый', 4: '4 - Зеленый', 
5: '5 - Голубой', 6: '6 - Синий', 7: '7 - Фиолетовый'}

for color in list_of_choice.values():
    print(color)
a = int(input('Номер выбранного цвета: '))

print('\n')

choice_of_figure = {1: '1 - Треугольник', 2: '2 - Квадрат', 3: '3 - Пятиугольник', 4: '4 - Шестиугольник'}
for figure in choice_of_figure.values():
    print(figure)
b = int(input('Выберите желаемую фигуру: '))
if b <= 4:
    if b == 1:  
        if a in list_of_colors:
            sp_triangle = sd.Point(250, 250)
            for i in range(30, 360, 120):
                gsp_triangle = sd.get_vector(sp_triangle, angle = i, length = 50, width = 3)
                gsp_triangle.draw(list_of_colors[a])
                sp_triangle = gsp_triangle.end_point
    if b == 2:  
        if a in list_of_colors:    
            sp_square = sd.Point(250, 250)
            for i in range(30, 360, 90):
                gsp_square = sd.get_vector(sp_square, angle = i, length = 50, width = 3)
                gsp_square.draw(list_of_colors[a])
                sp_square = gsp_square.end_point
    if b == 3:     
        if a in list_of_colors:
            sp_pentagon = sd.Point(250, 250)
            for i in range(30, 360, 72):
                gsp_pentagon = sd.get_vector(sp_pentagon, angle = i, length = 50, width = 3)
                gsp_pentagon.draw(list_of_colors[a])
                sp_pentagon = gsp_pentagon.end_point
    if b == 4:  
        if a in list_of_colors:
            sp_hexagon = sd.Point(250, 250)
            for i in range(30, 360, 60):
                gsp_hexagon = sd.get_vector(sp_hexagon, angle = i, length = 50, width = 3)
                gsp_hexagon.draw(list_of_colors[a])
                sp_hexagon = gsp_hexagon.end_point

    sd.pause()
else:
    print("Введен некорректный номер\n")