def smallest_multiple(n: int) -> int:
    for i in range(n, 1_000_000_000):
        found = True
        for j in range(1, n):
            if i % j != 0:
                found = False
                break
        if found:
            return i

    return -1


print(smallest_multiple(10))
print(smallest_multiple(20))
