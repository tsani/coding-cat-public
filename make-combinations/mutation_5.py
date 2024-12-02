def make_combinations(letters, numbers):
    '''
    Mistakenly uses tuple instead of list for the output.
    '''
    return [(letter, number) for letter in letters for number in numbers]