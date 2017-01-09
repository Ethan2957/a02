"""
Problem:

    The function 'powers' takes an integer input, n, between 1 and 100.
    If n is a square number, it should print 'Square'
    If n is a cube number, it should print 'Cube'
    If n is both square and cube, it should print 'Square and Cube'.
    For anything else, print 'Not a power'

    Cube numbers less than 100 are: 1, 8, 27, 64.

Tests:

    >>> powers(4)
    Square
    >>> powers(8)
    Cube
    >>> powers(53)
    Not a power
    >>> powers(27)
    Cube
    >>> powers(81)
    Square
    >>> powers(64)
    Square and Cube
    >>> powers(93)
    Not a power

"""

# This code tests your solution. Don't edit it.
import doctest
def run_tests():
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)


def powers(n):
    if n == 1 or n == 64:
        print('Square and Cube')
    elif n == 4 or n == 9 or n == 16 or n == 25 or n == 36 or n == 49 or n == 81:
        print('Square')
    elif n == 8 or n == 27:
        print('Cube')
    else:
        print('Not a power')


