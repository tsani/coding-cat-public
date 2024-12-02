def count_vowels(string):
    '''
    Mutation 1: Wrong condition check
    '''
    vowels = 'aeiouyAEIOUY'

    return sum(1 for char in string if char == vowels)
