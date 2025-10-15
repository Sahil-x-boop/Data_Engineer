import math


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    else:
        return True


num = int(input("Enter a number to check it it is Prime or Not: "))

if (is_prime(num)):
    print(f"{num} is Prime ")
else:
    print(f"{num} is Not Prime")

# One More Way
# def is_prime(n):
#     if (n <= 1):
#         return False
#     if (n <= 3):
#         return True

#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i += 1
#     return True

# num = int(input("Enter a number to check it it is Prime or Not: "))

# if (is_prime(num)):
#     print(f"{num} is Prime ")
# else:
#     print(f"{num} is Not Prime")
