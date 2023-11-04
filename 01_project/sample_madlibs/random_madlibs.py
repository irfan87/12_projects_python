the_zen = """Adjective: {adjective}\nNoun: {noun}\nVerb: {verb}"""


def madlibs():
    words = {
        "adjective": input("Enter the adjective: "),
        "noun": input("Enter the noun: "),
        "verb": input("Enter the verb: "),
    }
    # the_zen.format(**words) will replace the placeholders - {adjective}, {noun} and {verb} to the actual words
    # for instance: Adjective: {adjective} -> Adjective: colorful
    filled_story = the_zen.format(**words)

    print(filled_story)


if __name__ == "__main__":
    print("Random Madlibs\n")

    madlibs()
