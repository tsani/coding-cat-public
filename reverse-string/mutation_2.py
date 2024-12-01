def reverse_string(s):
    '''
    Simple mistake, this skips over the last letter
'''

    reversed_s = ""
    for char in s[:-1]:
        reversed_s = char + reversed_s
    return reversed_s
