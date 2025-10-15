# prime.py
import logging


logging.basicConfig(
    level=logging.DEBUG,
    filename="prime.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s  %(name)s - %(message)s"
)


def is_prime(n):
    logging.info(f"Checking if {n} is prime")
    if n <= 1:
        logging.warning("Number less than or equal to 1, not prime")
        return False
    for i in range(2, n):
        if n % i == 0:
            logging.debug(f"Divisible by {i}")
            return False
    return True


print(is_prime(44))
print(is_prime(1))
