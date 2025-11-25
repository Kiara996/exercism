def egg_count(display_value):
    egg_value = 0
    while display_value > 0:
        if display_value % 2 == 1:
            egg_value += 1
            display_value = display_value // 2
        else:
            display_value = display_value // 2
    return egg_value