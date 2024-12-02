def make_combinations(letters, numbers):
    '''
    Swaps the logic when creating the output pairs, which will result in a different order of the output pairs since the inner loop is now iterating over 'letters' instead of 'numbers'.
    '''
    return [[letter, number] for number in numbers for letter in letters]
