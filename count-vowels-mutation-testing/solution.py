def count_vowels(string):
    vowels = 'aeiouyAEIOUY'
    return sum(1 for char in string if char in vowels)
