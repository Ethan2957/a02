"""
Problem:

    The function 'letter_count' takes two inputs:
        * A message
        * A set of characters to test for

    The function should loop through each character in the message and print
    out the total number of times characters from the test set appear.

    e.g. letter_count("hello world", "ol") = 5 because there are two 'o's and
         three 'l's, for a total of 5.

    Hint: The 'in' keyword will be useful here.

Tests:

    >>> letter_count("hello world", "ol")
    5
    >>> letter_count("peter piper picked a peck of pickled pepper", "p")
    9
    >>> letter_count("humpty dumpty sat on a wall", "atu")
    8
    >>> letter_count("jack and jill went up the hill", "jl")
    6
    >>> letter_count("little bo peep has lost her sheep", "")
    0


"""

# This code tests your solution. Don't edit it.
import doctest
def run_tests():
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)


def letter_count(message, chars):
    count = 0
    meslength = len(message)
    charslength = len(chars)
    for char in range(meslength):
        for charss in range(charslength):
            if chars in message:
                count= count +1

    print(count)
