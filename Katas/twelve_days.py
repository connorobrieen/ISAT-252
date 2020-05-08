def recite(start_verse, end_verse):
    days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh",
            "eighth", "ninth", "tenth", "eleventh", "twelfth"]

    gifts = ["a Partridge in a Pear Tree", "two Turtle Doves",
            "three French Hens", "four Calling Birds",
            "five Gold Rings", "six Geese-a-Laying",
            "seven Swans-a-Swimming", "eight Maids-a-Milking",
            "nine Ladies Dancing", "ten Lords-a-Leaping",
            "eleven Pipers Piping", "twelve Drummers Drumming"]

    result = []

    for day in range(start_verse - 1, end_verse):

        days_gifts = gifts[day::-1]

        if len(days_gifts) > 1:
            days_gifts[-1] = "and {}".format(days_gifts[-1])

        result.append("On the {} day of Christmas my true love "
                    "gave to me: {}.".format(days[day],
                                            ", ".join(days_gifts)))
    return result