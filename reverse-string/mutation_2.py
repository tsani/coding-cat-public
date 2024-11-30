'''
simple mistake, this skips over the last letter
'''
def reverse_string(s):
    reversed_s = ""
    for char in s[:-1]:
        reversed_s = char + reversed_s
    return reversed_s
