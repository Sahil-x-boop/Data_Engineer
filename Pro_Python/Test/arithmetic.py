def perform_arithmetic_operation(s: str) -> int:
    char = s.split(" ")
    print(char)
    if char[1] == "+":
        return (int(char[0]) + int(char[2]))
    elif char[1] == "-":
        return (int(char[0]) - int(char[2]))
    elif char[1] == "*":
        return (int(char[0]) * int(char[2]))
    elif char[1] == "//":
        if int(char[2]) == 0:
            return -1
        return (int(char[0]) // int(char[2]))
    else:
        return None


value = ""
while value != "exit":
    value = input("Enter any arithmeti String to perform operation: ")
    print(perform_arithmetic_operation(value))

# word = "12 + 12"
# ch = word.split(" ")
# print(ch[1] == "+")
