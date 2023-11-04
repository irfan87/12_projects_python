import random

story = """
Once upon a time in a {adjective} land, there was a {noun} who loved to {verb}.
The {noun} had a {adjective} {noun} and a {noun} named {name}.
One day, they decided to {verb} to the {place} and found a {adjective} {noun}.
They all lived {adverb} ever after.
"""

adjectives = [
    "colorful",
    "sparkling",
    "mysterious",
    "magical",
    "exiciting",
]
nouns = [
    "unicorn",
    "horse",
    "dragon",
    "castle",
    "wizard",
]
verbs = [
    "dance",
    "fly",
    "sing",
    "explore",
    "dream",
]
names = [
    "alice",
    "bob",
    "ella",
    "max",
    "luna",
]
places = [
    "enchanted forest",
    "far-off kingdom",
    "magic land",
    "wonderful island",
    "fantasy world",
]
adverbs = [
    "happily",
    "gracefully",
    "curiously",
    "joyfully",
    "eagerly",
]


def random_generated_madlibs():
    generated_words = {
        "adjective": random.choice(adjectives),
        "noun": random.choice(nouns),
        "verb": random.choice(verbs),
        "name": random.choice(names),
        "place": random.choice(places),
        "adverb": random.choice(adverbs),
    }
    filled_generated_words = story.format(**generated_words)
    print(filled_generated_words)


if __name__ == "__main__":
    print("Random generated madlibs\n")
    random_generated_madlibs()
