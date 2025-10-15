from log_utils.extend_logging import logger


def fibonacci_upto(num):
    logger.debug("Get range of Fibonacci Series upto %d", num)
    if num < 0:
        logger.warning("Enter Positive Number!")
        return
    a, b = 0, 1
    for i in range(num+1):
        print(a, end=" ")
        logger.info("a = %d and b = %d and their sum = %d", a, b, a+b)
        a, b = b, a + b


fibonacci_upto(0)
fibonacci_upto(7)
fibonacci_upto(-4)
