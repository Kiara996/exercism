def resistor_label(colors):
    COLORS_LIST = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    tolerance_list = {"grey": "0.05%", "violet": "0.1%", "blue": "0.25%",
                     "green": "0.5%", "brown": "1%", "red": "2%",
                     "gold": "5%", "silver": "10%"}

    final_value = ""
    final_str = ""
    suffix = "ohms"
    if len(colors) == 1:
        final_str = "0 ohms"
    else:    
        tolerance_color = colors[-1]
        tolerance_val = tolerance_list[tolerance_color]
    
        multiplier_color = colors[-2]
        zero = COLORS_LIST.index(multiplier_color)
    
        digit_colors = colors[:-2]
    
        for color in digit_colors:
            value = COLORS_LIST.index(color)
            final_value += str(value)
    
        value = int(final_value) * (10**zero)
    
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
    
        final_str = (f"{value} {suffix} ±{tolerance_val}") 

    return final_str

    