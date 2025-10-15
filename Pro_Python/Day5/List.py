# student = ("Alice", 20, ["Math", "Science", "English"])
# print(student[2])

# def nonNegativeAverage(arr):
#     total = 0
#     count = 0
#     for num in arr:
#         if (num > 0):
#             total += num
#             count += 1
#     return total/count


# matrix = [[1, 2, 3],
#           [4, 5, [4, 6], 6],
#           [7, 8, 9]]


# def solve(matrix):
#     res = []
#     for row in matrix:
#         if isinstance(row, list):
#             res.append(row)
#         else:
#             res.extend(solve(row))
#     return res


# print(solve(matrix))

# li = ['a', 'b', 'c', 'd', 'e']

# print(li[10:])

# import sys

# lst = [1]
# tup = (1,)

# print("List size:", sys.getsizeof(lst))
# print("Tuple size:", sys.getsizeof(tup))


'''
if a tuple contains a mutable element (like a list), that list can change:
'''

# t = (1, [2, 3], 4)
# t[1][0] =
# print(t)

'''
Tuples themselves are immutable, but objects inside them can still mutate
'''


# def divide(a, b):
#     q = a / b
#     r = a % b
#     return (q, r)

# print(divide(20, 4))


# point = (3, 4)
# a, b = point
# print(a, b)

# a, b, c = 5, 6, 7
# print(a, c, b)

'''
count(x) → returns number of times x appears

index(x) → returns index of first occurrence of x
'''

# matrix = [
#     [1, 2, 3],
#     [3, 6, 2],
#     [6, 43, 9]
# ]

# print(matrix[2][1])

# cubes = [x*x*x for x in range(1, 6)]
# print(cubes)

# list1 = [1, 2, 3, 4, 5, 10]
# list2 = [3, 6, 9, 12, 15, 18]

# list1.extend(list2)
# list2.append(21)

# list3 = list1.copy()
# list4 = list3[::-1]
# print(list1, list2, list3, list4, sep=" \n")
