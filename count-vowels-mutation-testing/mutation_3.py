def count_vowels(string):
    '''
    Mutation 3: overcounting characters
    '''
    vowels = 'aeiouyAEIOUY'
    return sum(2 for char in string if char in vowels)
