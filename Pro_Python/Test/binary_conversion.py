def to_binary(num: int) -> str:
    binary = []
    while num > 0:
        bit = num % 2
        binary.append(str(bit))
        num //= 2
    return "".join(reversed(binary))


print(to_binary(48))


def now_binary(num: int) -> str:
    binary = ""
    while num > 0:
        bit = num % 2
        binary = str(bit) + binary
        num = num // 2
    return binary


print(now_binary())
