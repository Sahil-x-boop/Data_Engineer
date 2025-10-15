def is_pangram(text: str) -> bool:
    unique = set(char.lower() for char in text.lower() if char.isalpha())
    print(unique)
    return len(unique) == 26


pangrams = [
    "The big dwarf only jumps.",
    "Pack my box with jugs of liquor.",
    "The quick foxes climb steep hills.",
    "Quick foxes climb steep hillsides.",
    "The quick brown fox jumps over a lazy dog.",
    "Amazing ef acrobats always attempt bizarre acts at annual assemblies."
]

for text in pangrams:
    print(is_pangram(text))
