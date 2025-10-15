list1 = ["a", 1, "b", 2]

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

print({*list1})

merged = {**dict1, **dict2}
print(merged)
