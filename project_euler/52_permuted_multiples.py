def permuted_multiples():
    for i in range(1, 1_000_000):
        if sorted(str(2 * i)) == sorted(str(3 * i)) == sorted(str(4 * i)) == sorted(str(5 * i)) == sorted(str(6 * i)):
            return i
    return -1


print(permuted_multiples())
