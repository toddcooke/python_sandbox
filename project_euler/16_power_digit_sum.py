import math


def power_digit_sum(n):
    return sum(int(i) for i in list(str(int(math.pow(2, n)))))


print(power_digit_sum(15))
print(power_digit_sum(1000))
