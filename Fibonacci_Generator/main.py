import time


# -> printing the first n term os fib seq
def generate_fib_sequence(n: int) -> list[int]:  # n is one indexed
    start = time.time()
    fib = [0] * n  # empty list with dummy values of 0
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i - 2] + fib[i - 1]
    end = time.time()
    print(f"Time to print first {n} terms of the fibonacci sequence: {end - start}")
    return fib


def print_list(arr: list):
    for term in arr:
        print(f"{term} ", end="")
    print()


# NOTE THAT I AM WORKING WITH ZERO INDEX
# 0 1 1 2 3 5 ->sequence
# 0 1 2 3 4 5 ->indices
def fib1(n: int):
    if n <= 1:
        return n
    return fib1(n - 1) + fib1(n - 2)


# THIS TAKES NORMAL INDICES
# 0 1 1 2 3 5 ->sequence
# 1 2 3 4 5 6 ->indices
def fib1_test(n: int):
    start = time.time()
    print(f"Term number {n}: {fib1(n - 1)}")
    end = time.time()
    print(f"Time taken with fib1 function: {end - start}")


def fib2(n: int):
    if n <= 1:
        return n
    prev1 = 0
    prev2 = 1

    for i in range(2, n + 1):  # n - 2 + 1 = n-1 iterations
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current
    return current


def fib2_test(n: int):
    start = time.time()
    print(f"Term number {n}: {fib2(n - 1)}")
    end = time.time()
    print(f"Time taken with fib2 function: {end - start}")


num = int(input("Enter n: "))

# i must be positive
fib1_test(num)
fib2_test(num)
print_list(generate_fib_sequence(num))

