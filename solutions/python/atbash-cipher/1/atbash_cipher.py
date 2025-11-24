def encode(plain_text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"

    result = ""

    for char in plain_text.lower():
        if char in plain:
            index = plain.index(char)
            result += cipher[index]
        elif char.isdigit():
            result += char

    chunks = []
    for i in range(0, len(result), 5):
        grouping = result[i : i+5]
        chunks.append(grouping)

    return " ".join(chunks)


def decode(ciphered_text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"

    clean_cipher = ciphered_text.replace(" ", "")

    result = ""

    for char in clean_cipher:
        if char in cipher:
            index = cipher.index(char)
            result += plain[index]

        elif char.isdigit():
            result += char

    return result
