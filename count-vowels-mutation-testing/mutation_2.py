def count_vowels(string):
    '''
    Mutation 2: missing case for capital vowels
    '''
    vowels = 'aeiou'
    return sum(1 for char in string if char in vowels)
