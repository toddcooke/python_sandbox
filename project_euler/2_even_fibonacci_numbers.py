def fibonacci():
    one = 0
    two = 1
    while True:
        sum = one + two
        yield sum
        one = two
        two = sum


def even_fibonacci_numbers(max):
    fibs = []
    for fib in fibonacci():
        if fib > max:
            break
        if fib % 2 == 0:
            fibs.append(fib)
    return fibs


print(sum(even_fibonacci_numbers(4000000)))
