def is_prime(n: int):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def nth_prime(n: int):
    prime_count = 0
    i = 0
    while prime_count < n:
        i += 1
        if is_prime(i):
            prime_count += 1
    return i


print(nth_prime(6))
print(nth_prime(10001))
