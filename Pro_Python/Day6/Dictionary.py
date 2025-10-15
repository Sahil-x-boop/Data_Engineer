
# student = {
#     "name": "Sahil",
#     "roll_no": 101,
#     "marks": {"Math": 90, "English": 85, "Science": 92}
# }

# print(student["marks"]["Math"])
# print(student.get("marks", {}).get("Math"))

'''creates a new dictionary with specified keys
   and an optional default value for all keys.'''
# employee = dict.fromkeys(["emp_id", "age", "Role"], "Unknown")
# print(employee.items())

# person = {"name": "Sahil", "age": 22, "city": "Indore"}
# person.update({"country": "India"})
# for k, v in person.items():
#     print(k, v)

# print(person.items())

# person = {"name": "Sahil", "age": 22, "city": "Indore"}
# person.update({"country": "India"})
# print(person.items())


''' .get() avoids error if key doesn’t exist '''
# person = {"name": "Sahil", "age": 22, "city": "Indore"}
# print(person.get("birthday", "09-09-25"))


# Difference

'''
List → An ordered collection of items (indexed by numbers).

Dictionary → An unordered collection of key-value pairs (indexed by keys).'''


''' Hash value'''

# {[1, 2]: "A list as a key? Hmm..."}
# Traceback (most recent call last):
#     ...
# TypeError: unhashable type: 'list'
# hash values must remain constant for hashable types
