# Had to ask claude for this, my initial solution took forever
def largest_prime_factor(n: int) -> int:
    largest = 1
    # Peel off all the 2s so we can step by 2 afterwards
    while n % 2 == 0:
        largest = 2
        n //= 2
    # Now only odd candidates matter
    i = 3
    while i * i <= n:
        while n % i == 0:
            largest = i
            n //= i
        i += 2
    # Anything left over is itself prime
    if n > 1:
        largest = n
    return largest


print(largest_prime_factor(10))
print(largest_prime_factor(600_851_475_143))
