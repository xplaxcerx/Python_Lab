def calculate_tiles(area, tile_width, tile_length, price_per_tile):
    num_tiles = int(area / (tile_width * tile_length)) + 1
    total_cost = num_tiles * price_per_tile
    return (num_tiles, total_cost)
