#returning only the sum instead of the whwole list with the sum
def add_evens(numbers):
    total = 0
    for x in numbers:
        if x % 2 == 0:
            total = total + x
    return total
