def ran(start, end):
    if start > end:
        start, end = end, start
    product = 1
    for num in range(start, end + 1):
        product *= num
    return product


print("Product of numbers in a range:", ran(5, 2))
