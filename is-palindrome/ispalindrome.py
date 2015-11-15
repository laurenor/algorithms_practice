"""Is this word a palindrome?"""


def is_palindrome(word):
    """Return True/False if this word is a palindrome.

        >>> is_palindrome("a")
        True

        >>> is_palindrome("noon")
        True

        >>> is_palindrome("racecar")
        True

        >>> is_palindrome("porcupine")
        False

    Treat spaces and uppercase letters normally:

        >>> is_palindrome("Racecar")
        False
    """
    list_word = list(word.lower())
    for i in range(len(word)/2):
        temp = list_word[i]
        list_word[i] = list_word[-i-1]
        list_word[-i-1] = temp
    reversed_word = "".join(list_word)
    # print reversed_word
    if reversed_word == word:
        return True
    else:
        return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!"
