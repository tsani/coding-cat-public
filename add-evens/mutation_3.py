#Wrong indentation so the sum will be appended each time and not only at the end
def add_evens(numbers):
    total = 0
    for x in numbers:
        if x % 2 == 0:
            total = total + x
            numbers.append(total)
    return numbers
