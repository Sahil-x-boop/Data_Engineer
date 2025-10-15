from collections import Counter


def first_non_duplicate(word: str):
    count = Counter(word)
    for w in word:
        if count[w] == 1:
            return w


print(first_non_duplicate("alphlpha"))

# def first_non_duplicate(word: str):
#     freq = {}
#     for w in word:
#         freq[w] = freq.get(w, 0)+1
#     for w in word:
#         if freq[w] == 1:
#             return w


# print(first_non_duplicate("miami"))
