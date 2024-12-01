def remove_vowels(word: str, y_is_a_vowel: bool) -> str:
    '''
    Omitting to check for spaces in the word
    '''
    vowels = "aeiouAEIOU"
    vowels += "yY" if y_is_a_vowel else ""
    result = ""
    for letter in word: # or letter == " "     is missing
        if letter not in vowels:
            result += letter
    return result