def calculate_laminate(area, plank_width, plank_length, price_per_plank):
    num_planks = int(area / (plank_width * plank_length)) + 1
    total_cost = num_planks * price_per_plank
    return (num_planks, total_cost)
