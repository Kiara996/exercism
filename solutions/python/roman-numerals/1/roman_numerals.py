def roman(number):
    romans_num = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

    result = ""

    for value, romans in romans_num:
        while number >= value:
            result += romans
            number -= value

    return result