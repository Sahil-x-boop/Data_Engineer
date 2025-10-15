def generate_prime(x, y):
    for n in range(x, y):
        def is_prime(n):
            if n < 2:
                return False
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True
        if is_prime(n):
            print(n)


while True:
    user_input = input(
        "Enter any range to check prime numbers in it "
        "or press n to exit: "
    )
    if user_input.lower() == 'n':
        break
    try:
        x_str, y_str = user_input.strip().split()
        x, y = int(x_str), int(y_str)
        if x > y:
            x, y = y, x
        generate_prime(x, y)
    except ValueError:
        print("Invalid input please enter two number"
              "with a space between it or n to exit")
