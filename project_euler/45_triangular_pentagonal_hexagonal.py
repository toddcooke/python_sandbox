def tri():
    n = 1
    while True:
        yield int(n * (n + 1) / 2)
        n += 1


def pent():
    n = 1
    while True:
        yield int(n * (3 * n - 1) / 2)
        n += 1


def hex():
    n = 1
    while True:
        yield int(n * (2 * n - 1))
        n += 1


def triangular_pentagonal_hexagonal(previous_largest: int):
    ts = set()
    ps = set()
    hs = set()

    for t, p, h in zip(tri(), pent(), hex()):
        print(t, p, h)
        ts.add(t)
        ps.add(p)
        hs.add(h)
        intersection = sorted(list(ts.intersection(ps, hs)))
        if intersection[-1] > previous_largest:
            return intersection[-1]
    return -1


print(triangular_pentagonal_hexagonal(40754))
