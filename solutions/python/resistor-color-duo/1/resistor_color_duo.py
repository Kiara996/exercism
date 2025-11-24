def value(colors):
    COLORS_LIST = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    color1 = COLORS_LIST.index(colors[0])
    color2 = COLORS_LIST.index(colors[1])

    combine_index = str(color1) + str(color2)

    return int(combine_index)
