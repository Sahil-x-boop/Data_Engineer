

''' you can use the output of repr() to re-create the object stored in john '''

# john = Person("John Doe", 35)

# repr(john)
# "Person(name='John Doe', age=35)"

# str(john)
# "I'm John Doe, and I'm 35 years old."

"""
1. Use f-strings for formatting (cleaner & faster than format()).
2. Avoid + concatenation in loops → use str.join() for efficiency.
3. Normalize text before comparisons (.casefold() for case-insensitive checks).
4. For large text, prefer streaming (readline()) instead of read().
5. Use .strip() when handling user input.
"""
