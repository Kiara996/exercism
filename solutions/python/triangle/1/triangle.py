def equilateral(sides):
    a, b, c = sides
    is_valid = (a > 0 and b > 0 and c > 0) and (a + b >= c and b + c >= a and a + c >= b)
    if not is_valid:
        return False
    return a == b and b == c


def isosceles(sides):
    a, b, c = sides
    is_valid = (a > 0 and b > 0 and c > 0) and (a + b >= c and b + c >= a and a + c >= b)
    if not is_valid:
        return False
    return a == b or  b == c or a == c


def scalene(sides):
    a, b, c = sides
    is_valid = (a > 0 and b > 0 and c > 0) and (a + b >= c and b + c >= a and a + c >= b)
    if not is_valid:
        return False
    return a != b and b != c and a != c
