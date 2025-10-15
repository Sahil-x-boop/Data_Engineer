def is_armstrong(num):
    if num < 1:
        return False
    old_num = num
    cube = 0
    while num > 0:
        rem = num % 10
        cube += rem**3
        num //= 10
    if old_num == cube:
        return True
    return False


def generate_armstrong(num1, num2):
    for num in range(num1, num2 + 1):
        if is_armstrong(num):
            print(num)


while True:
    user_input = input(
        "Enter any range to check armstrong numbers in it "
        "or press n to exit: "
    )
    if user_input.lower() == "n":
        break
    try:
        x_str, y_str = user_input.strip().split()
        x, y = int(x_str), int(y_str)
        if x > y:
            x, y = y, x
        generate_armstrong(x, y)
    except ValueError:
        print(
            "Invalid input please enter two number"
            "with a space between it or n to exit"
        )
