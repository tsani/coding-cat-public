def count_vowels(string):
    '''
    Mutation 1: mispelled vowels
    '''
    viwels = 'aeiouyAEIOUY'

    return sum(1 for char in string if char in vowels)
