def recite(start_verse, end_verse):
    day_list = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

    gift_list = ["a Partridge in a Pear Tree.", "two Turtle Doves, ", "three French Hens, ", "four Calling Birds, ", "five Gold Rings, ", "six Geese-a-Laying, ", "seven Swans-a-Swimming, ", "eight Maids-a-Milking, ", "nine Ladies Dancing, ", "ten Lords-a-Leaping, ", "eleven Pipers Piping, ", "twelve Drummers Drumming, "]

    lyrics = []

    for verse in range(start_verse, end_verse + 1):
        day_name = day_list[verse - 1]
        line = (f"On the {day_name} day of Christmas my true love gave to me: ")
        for i in range(verse - 1, -1, -1):
            if i == 0 and verse > 1:
                line += "and "
            line += gift_list[i]

        lyrics.append(line)

    return lyrics