'''
By doing reversed_s += char, it just duplicated the original string instead of chaning the order.
'''
def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s += char
    return reversed_s
