def transform(legacy_data):
    new_data = {}

    for score, letters in legacy_data.items():
        for letter in letters:
            lowercase_letter = letter.lower()
            new_data[lowercase_letter] = score

    return new_data
