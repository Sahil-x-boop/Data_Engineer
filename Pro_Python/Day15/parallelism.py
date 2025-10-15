import threading

counter = 0
lock = threading.Lock()


def worker(n):
    global counter
    lock.acquire()
    for _ in range(n):
        counter += 1
    lock.release()


if __name__ == "__main__":
    N_THREADS = 10
    INCREMENTS = 1000000

    threads = []
    for i in range(N_THREADS):
        t = threading.Thread(target=worker, args=(INCREMENTS,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Expected:", N_THREADS * INCREMENTS)
    print("Actual:  ", counter)

# import multiprocessing
# import time
# import math
# import sys

# sys.set_int_max_str_digits(1000000)


# def calc_factorial(n):
#     print(f"[{multiprocessing.current_process().name}] Calculating Factorial of {n}")
#     result = math.factorial(n)
#     print(f"Factorial of {n}! is {result}")


# if __name__ == "__main__":
#     numbers = [20000, 7500, 2000, 4000, 8000, 7000, 11000, 330000, 90000]

#     start_time = time.time()
#     processes = []

#     for n in numbers:
#         process = multiprocessing.Process(target=calc_factorial, args=(n,))
#         processes.append(process)
#         process.start()

#     for process in processes:
#         process.join()

#     print(processes)
#     print(f"Time Taken: {time.time() - start_time} Seconds")

# import threading
# import time
# import math
# import sys

# sys.set_int_max_str_digits(1000000)


# def calc_factorial(n):
#     print(f"[{threading.current_thread().name}] Calculating Factorial of {n}")
#     result = math.factorial(n)
#     print(f"Factorial of {n}! is {result}")


# if __name__ == "__main__":
#     numbers = [20000, 7500, 2000, 4000, 8000, 7000, 11000, 330000, 90000]

#     start_time = time.time()
#     threads = []

#     for n in numbers:
#         thread = threading.Thread(target=calc_factorial, args=(n,))
#         threads.append(thread)
#         thread.start()

#     for thread in threads:
#         thread.join()

#     print(threads)
#     print(f"Time Taken: {time.time() - start_time} Seconds")

