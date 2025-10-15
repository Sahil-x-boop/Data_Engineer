def is_palindrome(word: str) -> bool:
    word = word.casefold()
    return word == word[::-1]


word = ""
while word.lower() != "exit":
    word = input("Enter any word to check it is palindrome or not: ")
    print(is_palindrome(word))
