def sum_of_multiples(level, factors):
    unique_multiples = set()
    for item in factors:
        if item == 0:
            continue

        for multiple in range(item, level, item):
            unique_multiples.add(multiple)
            
    return sum(unique_multiples)