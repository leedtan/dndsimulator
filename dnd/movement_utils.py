def place_closest_position(char, coor, table):
    table[table == char] = 0
    if table[coor] == 0:
        char.coor = coor
        table[coor] = char
    else:
        for distance in range(1, 5):
            new_position = get_closest_within_dist(coor, distance, table, char)
            if len(new_position) > 0 and table[new_position[0]] == 0:
                char.coor = new_position[0]
                table[new_position[0]] = char
                return
        raise ValueError("couldn't find a place to lie")


def get_closest_within_dist(coor, distance, table, char):
    min_x, max_x = coor[0] - distance, coor[0] + distance
    min_y, max_y = coor[1] - distance, coor[1] + distance
    options = [(x, y_extreme) for x in range(min_x, max_x + 1) for y_extreme in [min_y, max_y]] + [
        (x_extreme, y) for y in range(min_y + 1, max_y) for x_extreme in [min_x, max_x]
    ]
    options = [
        option
        for option in options
        if option[0] >= 0 and option[1] >= 0 and option[0] < table.shape[0] and option[1] < table.shape[1]
    ]
    options = [option for option in options if table[option] == 0 or table[option] == char]
    return options
