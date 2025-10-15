""""p.one.two.three" → "<p class='one two three'></p>"."""


def secret(text: str):
    word = text.strip().split('.')
    print(word)
    classes = " ".join(word[1:])
    if word[0].lower() == 'p':
        print(f"<p class='{classes}'></p>")


word = input("Enter: ")
print(secret(word))
