def special_pythagorean_triplet(sum):
    for a in range(1, sum + 1):
        a_squared = a * a
        for b in range(1, sum + 1):
            b_squared = b * b
            for c in range(1, sum + 1):
                c_squared = c * c
                if a_squared + b_squared == c_squared and a + b + c == sum:
                    return a * b * c
    return -1


print(special_pythagorean_triplet(1000))
