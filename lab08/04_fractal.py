# -*- coding: utf-8 -*-

import simple_draw as sd
import random
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код
sd.resolution = (1200, 600)
root_point  = sd.get_point(300, 30)
def draw_branches(start_point, p_angle, p_length):
    if p_length < 10:
        return None
    fv = sd.get_vector(start_point, p_angle, p_length)
    sv = sd.get_vector(start_point, p_angle, p_length)
    fv.draw()
    sv.draw()
    nv = fv.end_point
    nv2 = sv.end_point
    draw_branches(nv, p_angle=p_angle-48, p_length=(p_length*0.75))
    draw_branches(nv2, p_angle=p_angle+48, p_length=(p_length*0.75))
draw_branches(start_point=root_point, p_angle=80, p_length=140)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см results/exercise_04_fractal_02.jpg

# Пригодятся функции
#sd.random_number()

sd.pause()
