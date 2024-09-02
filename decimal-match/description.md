Write a function `decimal_match(n: int, f: float) -> bool` that takes two inputs: an integer `n` and a floating-point number `f`. The function should return `True` if the decimal part of `f` contains the integer `n` in sequence; otherwise, it should return `False`. For example, if the inputs are `11` and `0.11`, the output should be `True` because `11` appears in the decimal part of `0.11`. 

**Note:** the int will always be two digits long, and the deciaml will only only have 2 digits in
the decimal part, ex 11 and 0.11 and never 111 and 0.111 or larger. 
