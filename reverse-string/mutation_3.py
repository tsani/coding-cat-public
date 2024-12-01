def reverse_string(s):
    '''
By doing reversed_s += char, it just duplicated the original string instead of chaning the order.
'''

    reversed_s = ""
    for char in s:
        reversed_s += char
    return reversed_s
