def self_powers(n: int):
    return sum([i ** i for i in range(1, n + 1)])


print(self_powers(10))
print(self_powers(1000))
