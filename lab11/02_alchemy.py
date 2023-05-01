# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код
class Вода:
    def __str__(self):
        return "Вода"
    
    def __add__(self, other):
        if isinstance(other, Воздух):
            return Шторм()
        elif isinstance(other, Огонь):
            return Пар()
        elif isinstance(other, Земля):
            return Грязь()
        else:
            return None

class Воздух:
    def __str__(self):
        return "Воздух"
    
    def __add__(self, other):
        if isinstance(other, Огонь):
            return Молния()
        elif isinstance(other, Земля):
            return Пыль()
        elif isinstance(other, Вода):
            return Шторм()
        else:
            return None

class Огонь:
    def __str__(self):
        return "Огонь"
    
    def __add__(self, other):
        if isinstance(other, Земля):
            return Лава()
        elif isinstance(other, Вода):
            return Пар()
        elif isinstance(other, Воздух):
            return Молния()
        else:
            return None

class Земля:
    def __str__(self):
        return "Земля"
    
    def __add__(self, other):
        if isinstance(other, Вода):
            return Грязь()
        elif isinstance(other, Воздух):
            return Пыль()
        elif isinstance(other, Огонь):
            return Лава()
        else:
            return None

class Шторм:
    def __str__(self):
        return "Шторм"

class Пар:
    def __str__(self):
        return "Пар"

class Грязь:
    def __str__(self):
        return "Грязь"

class Молния:
    def __str__(self):
        return "Молния"

class Пыль:
    def __str__(self):
        return "Пыль"

class Лава:
    def __str__(self):
        return "Лава"

# Ввод элементов пользователем
print("выберите элементы:\nВода\nВоздух\nОгонь\nЗемля\n")
elem1 = input("Введите первый элемент: ")
elem2 = input("Введите второй элемент: ")

# Создание объектов элементов
if elem1.lower() == "вода":
    elem1_obj = Вода()
elif elem1.lower() == "воздух":
    elem1_obj = Воздух()
elif elem1.lower() == "огонь":
    elem1_obj = Огонь()
elif elem1.lower() == "земля":
    elem1_obj = Земля()
else:
    print("Некорректный первый элемент")
    elem1_obj = None

if elem2.lower() == "вода":
    elem2_obj = Вода()
elif elem2.lower() == "воздух":
    elem2_obj = Воздух()
elif elem2.lower() == "огонь":
    elem2_obj = Огонь()
elif elem2.lower() == "земля":
    elem2_obj = Земля()
else:
    print("Некорректный второй элемент")
    elem2_obj = None

# Вычисление результата и вывод на экран
if elem1_obj and elem2_obj:
    result = elem1_obj + elem2_obj
    if result:
        print(elem1_obj, "+", elem2_obj, "=", result)
else:
    print("Не удалось объединить элементы")

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
