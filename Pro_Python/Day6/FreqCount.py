sentence = "python is great and python is easy to learn"

words = sentence.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(f"Word Frequency: {freq}")
