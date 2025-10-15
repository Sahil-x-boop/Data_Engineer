def is_leap_year(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False


for year in [2000, 1998, 1886, 1440, 2028]:
    print(year, is_leap_year(year))

# def max_of_three(a, b, c):
#     if b <= a >= c:
#         return a
#     elif a <= b >= c:
#         return b
#     else:
#         return c


# print(max_of_three(7, 9, 4))

# -------------------------------------

# def left():
#     print("Left Evaluated")
#     return False


# def right():
#     print("Right Evaluated")
#     return True


# print(left() or right())


# def start(): print("Started")


# def stop(): print("Stopped")


# def pause(): print("paused")


# cmd = "stop"
# actions = {
#     "start": start,
#     "stop": stop,
#     "pause": pause
# }

# actions.get(cmd, lambda: print("Unknown Command"))()

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# word = "Python"
# for char in word:
#     print(char)

# ages = {"Alice": 30, "Bob": 25, "Charlie": 35}
# for name, age in ages.items():

#     print(f"{name} is {age} years old.")

# print("A" and "B")  # 'B' (both truthy → last)
# print("j" or "fallback")  # 'fallback' (first truthy)
# print((False or True))

# a = 3
# print(object.__sizeof__(a))
