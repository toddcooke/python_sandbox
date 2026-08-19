def largest_palindrome_product(n: int) -> int:
    top = -1
    for i in range((10 ** n) - 1, 1, -1):
        for j in range((10 ** n) - 1, 1, -1):
            print(i,j)
            product = str(i * j)
            if product == product[::-1]:
                if int(product) > top:
                    top = int(product)
    return top


# print(largest_palindrome_product(2))
print(largest_palindrome_product(3))
