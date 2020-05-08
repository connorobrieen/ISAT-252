""" a program that calculates word scores for scrabble"""

POINTS = {
    letter: value
    for letters, value in {
        "aeioulnrst": 1,
        "dg": 2,
        "bcmp": 3,
        "fhvwy": 4,
        "k": 5,
        "jx": 8,
        "qz": 10,
    }.items()
    for letter in letters
}


def score(word):
    return sum(POINTS[x] for x in word.lower())