Write a function `double_n-th(str,n)` that when given a string and an integer n, returns a new string where every n-th character position in the original string is doubled based on the following conditions:

- Normally, you return the string with every `n`-th character doubled.
- If `n` is greater than the string length, return the original string.
- If `n` is less than or equal to 0, return `""`.
- if `str` is empty, return `""`.


For example:
- If `(programming,2)` is inputted, the output is `prroggraammminng`.
- If `("two",2)`, is inputted, the output is `"twwo"`.
- If `("three",3)`, is inputted, the output is `"thrree"`.
- If `("hi",3)`, is inputted, the output is `hi`.
- If `("bonjour",-2)`, is inputted, the output is `""`.
- If `("null",0)`, is inputted, the output is `""`.
- If `("",-2)`, is inputted, the output is `""`.
