def product_of_numbers(n):
    return lambda a:a*n

product = product_of_numbers(6)
print(product(5))
