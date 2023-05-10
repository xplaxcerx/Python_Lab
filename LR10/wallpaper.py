def calculate_wallpaper(area, roll_width, roll_length, price_per_roll):
    num_rolls = int(area / (roll_width * roll_length)) + 1
    total_cost = num_rolls * price_per_roll
    return (num_rolls, total_cost)
