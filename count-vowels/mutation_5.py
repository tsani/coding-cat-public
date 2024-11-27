def count_vowels(string):
    lst = []
    for i in string:
        if i in ['aeiouyAEIOUY']:
            lst.pop(i) #pop instead of append
    return len(lst)