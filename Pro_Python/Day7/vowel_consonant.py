def count_vowel_consonant(word: str):
    vowels = set("aeiou")
    v_count = sum(1 for ch in word if ch in vowels)
    c_count = sum(1 for ch in word if ch.isalpha() and ch not in vowels)
    return v_count, c_count


word = ""
while word.lower() != "exit":
    word = input("Enter any word to check Vowel and Consonant count: ")
    x, y = count_vowel_consonant(word)
    print(f"There are {x} vowels and {y} consonants in {word}")
