def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return False
    return True


def summation_of_primes(n: int) -> int:
    total = 0
    for i in range(2, n):
        if is_prime(i): total += i
    return total


print(summation_of_primes(10))
print(summation_of_primes(2_000_000))
