def sum_square_difference(n):
    sum_of_squares = 0
    sum_of_range = 0
    for i in range(n + 1):
        sum_of_squares += i * i
        sum_of_range += i
    square_of_sum = sum_of_range * sum_of_range
    return square_of_sum - sum_of_squares


print(sum_square_difference(100))
