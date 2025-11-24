def label(colors):
    COLORS_LIST = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    digit1 = COLORS_LIST.index(colors[0])
    digit2 = COLORS_LIST.index(colors[1])
    digit3 = COLORS_LIST.index(colors[2])

    value = ((digit1) * 10 + (digit2)) * (10**(digit3))
    suffix = "ohms"

    if value >= 1000000000:
        value = value / 1000000000
        suffix = "gigaohms"
    elif value >= 1000000:
        value = value / 1000000
        suffix = "megaohms"
    elif value >= 1000:
        value = value / 1000
        suffix = "kiloohms"

    if int(value) == value:
        value = int(value)

    return (f"{value} {suffix}")
