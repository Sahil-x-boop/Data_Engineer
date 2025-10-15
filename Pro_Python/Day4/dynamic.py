

'''We don’t declare types explicitly.

The type is decided at runtime, depending on the object assigned.'''

# x = 10          # x is int
# x = "hello"     # now x is str
# x = [1, 2, 3]   # now x is list

''' A single variable can hold values of different types at different times.'''


def add(x: int, y: int) -> int:
    return x + y


print(add(10, 20))     # works
print(add("a", "b"))   # still runs, but type checkers (like mypy) will warn
