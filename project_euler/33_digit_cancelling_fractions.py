from math import gcd


# Used chatgpt answer this
def digit_cancelling_fractions():
    numerator = 1
    denominator = 1

    for n in range(10, 100):
        for d in range(n + 1, 100):
            # Ignore trivial cases involving zero
            if n % 10 == 0 or d % 10 == 0:
                continue

            n1, n2 = divmod(n, 10)
            d1, d2 = divmod(d, 10)

            # Try cancelling each common digit
            if n2 == d1 and n1 * d == n * d2:
                numerator *= n1
                denominator *= d2

            elif n1 == d2 and n2 * d == n * d1:
                numerator *= n2
                denominator *= d1

    g = gcd(numerator, denominator)
    return denominator // g


print(digit_cancelling_fractions())
