
# import gc

# a = {}
# b = {}

# a['ref'] = b
# b['ref'] = a

# del a
# del b


# collected = gc.collect()
# print(f" Garbage {collected} values")

a = 10
b = a
print(id(a), type(a), a)
print(id(b), type(b), b)
