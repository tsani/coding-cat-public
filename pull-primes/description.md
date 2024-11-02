
Write a function `primes(list)`, where the list contains 4 positive integers between 0 and 169 (not included), that determines if any of the numbers are primes and prints a new list that includes only the primes (make sure that the primes are in ascending order), if there are none, print `There are no prime numbers in this list`
For the sake of simplicity, assume that we only care for the prime factors 2, 3, 5, 7 and 11

For example:
- [1, 3, 12, 14] returns [1, 3]
- [12, 13, 41, 62] returns [13, 41]
- [12, 14, 16, 18] prints `There are no prime numbers in this list`

Hint: Modulo is required