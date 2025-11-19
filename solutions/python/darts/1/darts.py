def score(x, y):
    hypotenus = (x**2 + y**2)**0.5

    if hypotenus <= 1:
        return 10
    elif 1 < hypotenus <= 5:
        return 5
    elif 5 < hypotenus <= 10:
        return 1
    else:
        return 0