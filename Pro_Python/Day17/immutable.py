def add_item(*args, lst=None):
    if lst is None:
        lst = []
    lst.append(args)
    return lst

print(add_item(2))
print(add_item(4, 6))

