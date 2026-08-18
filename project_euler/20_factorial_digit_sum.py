def sum_factorial_digits(n: int):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return sum([int(i) for i in list(str(total))])


print(sum_factorial_digits(10))
print(sum_factorial_digits(100))
