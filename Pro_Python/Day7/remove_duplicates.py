def remove_duplicates(word: str):
    unique = set()
    return "".join(ch for ch in word if not (ch in unique or unique.add(ch)))


def remove_duplicate(word: str):
    unique = set(word)
    new = ""
    for ch in word:
        if ch in unique:
            new += ch
            unique.remove(ch)
    return new


word = ""
while word.lower() != "exit":
    word = input("Enter any word to get non repeated character string ")
    print(remove_duplicates(word))
