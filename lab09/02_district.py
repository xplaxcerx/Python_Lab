#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Составить список всех живущих на районе (пакет district) и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
import district.central_street.house1.room1, district.central_street.house1.room2, district.central_street.house2.room1, district.central_street.house2.room2, district.soviet_street.house1.room1, district.soviet_street.house1.room2, district.soviet_street.house2.room1, district.soviet_street.house2.room2

folks_in_the_area = []
for street in [district.central_street, district.soviet_street]:
    for house in [street.house1, street.house2]:
        for room in [house.room1, house.room2]:
            folks_in_the_area.extend(room.folks)
print("Жители на районе:", ", " .join(folks_in_the_area))

