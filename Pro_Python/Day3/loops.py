# 1.

# num = 12345
# total = 0
# for i in str(num):
#     total += int(i)
# print(total)

# num = 12345
# total = 0
# while num > 0:
#     digit = num % 10
#     total += digit
#     num = num//10
# print(total)

# 2.
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print("Factorial is", fact)


'''
- Use for i in range(n) when you only need iteration count.

- Use enumerate(iterable) instead of range(len(iterable))
  when you need index + value.
'''


# 3.
# lis = [14, 2, 85, 33]
# for i in range(len(lis)):
#     print(i, lis[i], sep=" ")

# for i, val in enumerate([14, 2, 85, 33]):
#     print(i, val, sep=" ")

# 4.
# for i in range(5):
#     if i == 3:
#         pass  # do nothing here
#     print("i =", i)

# 5.
# for i in range(3, 30, 3):
#     print(i)

# 6.
# user_input = ""
# while user_input.lower() != "exit":
#     user_input = input("Type Something or (exit to quit!): ").upper()
#     for char in user_input:
#         print(char)


# 7.
# user_input = ""
# while user_input.lower() != "exit":
#     user_input = input("Type Something or (exit to quit!): ")
#     print(f"You typed : {user_input}")

# 8.

# for i in range(5, 0, -1):
#     for j in range(0, 5):
#         print(" " * i)
#     print("*" * i)

# 9.

# def print_diamond(n):
#     for i in range(1, n + 1):
#         print(" " * (n - i) + "*" * (2 * i - 1))
#     for i in range(n - 1, 0, -1):
#         print(" " * (n - i) + "*" * (2 * i - 1))
