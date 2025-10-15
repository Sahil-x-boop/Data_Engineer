def remove_duplicates(word: str):
    unique = set(word)
    new = ""
    for ch in word:
        if ch in unique:
            new = "".join(chr)
            unique.remove(ch)
    return new


word = ""
while word.lower() != "exit":
    word = input("Enter any word to get non repeated character word: ")
    print(remove_duplicates(word))
