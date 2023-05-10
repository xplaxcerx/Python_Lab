from guizero import App, Text, TextBox, PushButton, info
from wallpaper import calculate_wallpaper
from tiles import calculate_tiles
from laminate import calculate_laminate

app = App(title="Калькулятор отделочных материалов")

area_text = Text(app, text="Площадь помещения (кв.м):")
roll_width_text = Text(app, text="Ширина рулона обоев (м):")
roll_length_text = Text(app, text="Длина рулона обоев (м):")
tile_width_text = Text(app, text="Ширина плитки (см):")
tile_length_text = Text(app, text="Длина плитки (см):")
plank_width_text = Text(app, text="Ширина доски ламината (см):")
plank_length_text = Text(app, text="Длина доски ламината (см):")
wallpaper_price_text = Text(app, text="Стоимость рулона обоев (руб):")
tile_price_text = Text(app, text="Стоимость плитки (руб/шт):")
laminate_price_text = Text(app, text="Стоимость доски ламината (руб/шт):")

area_box = TextBox(app, width=10)
roll_width_box = TextBox(app, width=10)
roll_length_box = TextBox(app, width=10)
tile_width_box = TextBox(app, width=10)
tile_length_box = TextBox(app, width=10)
plank_width_box = TextBox(app, width=10)
plank_length_box = TextBox(app, width=10)
wallpaper_price_box = TextBox(app, width=10)
tile_price_box = TextBox(app, width=10)
laminate_price_box = TextBox(app, width=10)
wallpaper_button = PushButton(app, text="Рассчитать обои")
tile_button = PushButton(app, text="Рассчитать плитку")
laminate_button = PushButton(app, text="Рассчитать ламинат")

def calculate_wallpaper_cost():
    try:
        area = float(area_box.value)
        roll_width = float(roll_width_box.value)
        roll_length = float(roll_length_box.value)
        price_per_roll = float(wallpaper_price_box.value)
        num_rolls, total_cost = calculate_wallpaper(area, roll_width, roll_length, price_per_roll)
        info("Результаты расчёта", f"Необходимо закупить {num_rolls} рулонов обоев на общую сумму {total_cost} рублей.")
    except ValueError:
        info("Ошибка", "Некорректный ввод.")
def calculate_tile_cost():
    try:
        area = float(area_box.value)
        tile_width = float(tile_width_box.value) / 100
        tile_length = float(tile_length_box.value) / 100
        price_per_tile = float(tile_price_box.value)
        num_tiles, total_cost = calculate_tiles(area, tile_width, tile_length, price_per_tile)
        info("Результаты расчёта", f"Необходимо закупить {num_tiles} плиток на общую сумму {total_cost} рублей.")
    except ValueError:
        info("Ошибка", "Некорректный ввод.")
def calculate_laminate_cost():
    try:
        area = float(area_box.value)
        plank_width = float(plank_width_box.value) / 100
        plank_length = float(plank_length_box.value) / 100
        price_per_plank = float(laminate_price_box.value)
        num_planks, total_cost = calculate_laminate(area, plank_width, plank_length, price_per_plank)
        info("Результаты расчёта", f"Необходимо закупить {num_planks} досок ламината на общую сумму {total_cost} рублей.")
    except ValueError:
        info("Ошибка", "Некорректный ввод.")
wallpaper_button.when_clicked = calculate_wallpaper_cost
tile_button.when_clicked = calculate_tile_cost
laminate_button.when_clicked = calculate_laminate_cost
app.display()

