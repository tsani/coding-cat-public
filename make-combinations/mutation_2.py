def make_combinations(letters, numbers):
    '''
    Mistakenly swaps the order of the loops, which will result in a different order of the output pairs.
    '''
    return [[letter, number] for number in numbers for letter in letters]
