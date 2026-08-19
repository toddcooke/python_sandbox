import math


def equals_own_factorial(n: int) -> bool:
    """n = 145 -> 1! + 4! + 5! == 145 -> True"""
    return n == sum([math.factorial(int(i)) for i in list(str(n))])


def digit_factorials():
    facts = []
    for i in range(3, 1_000_000):
        if equals_own_factorial(i):
            facts.append(i)
            print(facts)
    return sum(facts)


print(digit_factorials())
