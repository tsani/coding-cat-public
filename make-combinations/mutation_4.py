def make_combinations(letters, numbers):
    '''
    Mistakenly uses 'numbers' instead of 'letters' in the inner loop.
    '''
    return [[letter, number] for number in numbers for letter in numbers]
