import math


def digit_nth_powers(n):
    total = 0
    for i in range(2, 1_000_000):
        if i ==  sum([math.pow(int(i), n) for i in list(str(i))]):
            total += i
            print(i)
    return total


print(digit_nth_powers(4))
print()
print("total",digit_nth_powers(5))
