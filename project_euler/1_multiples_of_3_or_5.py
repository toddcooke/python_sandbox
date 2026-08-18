def multiples_of_3_or_5(n):
    mults = []
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            mults.append(i)
    return sum(mults)

print(multiples_of_3_or_5(10))
print(multiples_of_3_or_5(1000))
