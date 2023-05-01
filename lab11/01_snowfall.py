# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)
# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.pam = {'length': sd.random_number(10, 100),
        'x': sd.random_number(100, 1100),
        'y': 600 + sd.randint(100, 150)
        }
        self.snowflake = self.pam
    def clear_previous_picture(self):
        point = sd.get_point(self.snowflake['x'], self.snowflake['y'])
        sd.snowflake(center=point, color=sd.background_color, length = self.snowflake['length'])
    def move(self):
        self.snowflake['x'] -= sd.randint(-10, 10)
        self.snowflake['y'] -= sd.randint(10, 25)
        self.point = sd.get_point(self.snowflake['x'], self.snowflake['y'])  
    def draw(self):
        sd.snowflake(center=self.point,color=sd.COLOR_WHITE, length = self.snowflake['length']) 
    def can_fall(self):
        return 0 if self.snowflake['y'] < sd.random_number(15, 30) else 1
    # TODO здесь ваш код


flake = Snowflake()


while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# class Snowflake:
#     def __init__(self):
#         self.snowflake = {'length': sd.random_number(10, 100),
#         'x': sd.random_number(100, 1100),
#         'y': 600 + sd.randint(200, 600)
#         }
#     def clear_previous_picture(self):
#         point = sd.get_point(self.snowflake['x'], self.snowflake['y'])
#         sd.snowflake(center=point, color=sd.background_color, length = self.snowflake['length'])
#     def move(self):
#         self.snowflake['x'] -= sd.randint(-10, 10)
#         self.snowflake['y'] -= sd.randint(10, 25)
#         self.point = sd.get_point(self.snowflake['x'], self.snowflake['y'])  
#     def draw(self):
#         sd.snowflake(center=self.point,color=sd.COLOR_WHITE, length = self.snowflake['length']) 
#     def fallen(self):
#         return 1 if 0 < self.snowflake['y'] < sd.random_number(15, 30) else 0
#     # TODO здесь ваш код

# N = 20
# i = 0
# flakes = []

# for _ in range(N):
#     flakes.append(Snowflake())

# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#         if flake.fallen():
#             flakes.append(Snowflake())
# #     if fallen_flakes:
# #         append_flakes(count=fallen_flakes)
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break









sd.pause()
