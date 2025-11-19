def is_isogram(string):
    lower_string = string.lower()
    letters_list = []

    for char in lower_string:
        if char == ' ' or char == '-':
            continue

        if char in letters_list:
            return False

        letters_list.append(char)

    return True