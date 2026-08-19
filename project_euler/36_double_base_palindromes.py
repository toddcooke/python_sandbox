def double_base_palindromes(n: int) -> int:
    palindromes = []
    for i in range(n):
        s = str(i)
        b = f"{i:b}"
        print(s, b)
        # No leading 0s
        if b[0] == "0": continue
        # Need to convert to list to consume reversed iterator
        if list(s) == list(reversed(s)) and list(b) == list(reversed(b)):
            palindromes.append(i)
    return sum(palindromes)


print(double_base_palindromes(1_000_000))
