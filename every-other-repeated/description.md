Write a function `every_other_repeated(a, b)` that counts how many substrings of length two, formed by taking every other letter from string `a` match the last two letters of string `b`.

For example:
- 'a': "ooooo" ; 'b': "ooooo" ; returns 3
- 'a': "aabbaa" ; 'b': "baab" ; returns 2
- 'a': "loool" ; 'b': "hello" ; returns 1

**Note**: Every other letter means taking the letter, ignoring the one that follows, and taking the next. 
Ex. the sublists of lenght 2 of every other letter in "abcde" **->** "ac", "bd", "ce".
