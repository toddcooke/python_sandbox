# Had to ask chatgpt for the answer
def number_spiral_diagonals(n: int) -> int:
    # Need odd number for spiral
    if n < 3 or n % 2 == 0: return -1

    diagonal_sum = 1
    for layer in range(1, n // 2 + 1):
        side = 2 * layer + 1
        max_corner = side ** 2
        step = side - 1

        for _ in range(4):
            diagonal_sum += max_corner
            max_corner -= step

    return diagonal_sum


print(number_spiral_diagonals(5))
print(number_spiral_diagonals(1001))
