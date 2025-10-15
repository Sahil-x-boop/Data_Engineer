def check_anagram(word1: str, word2: str) :
    return (ch for ch in word1 if ch in word2)


print(bool(check_anagram("silent", "listen")))
