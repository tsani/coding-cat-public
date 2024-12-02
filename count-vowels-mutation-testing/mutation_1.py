def count_vowels(string):
    '''
    Mutation 1:
    '''
    vowels = 'aeiouyAEIOUY'

    return sum(1 for char in string if char in vowels)
