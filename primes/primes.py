def is_prime(num):
    """Is num a prime number?

    num will always be a positive integer.

    >>> is_prime(0)
    False

    >>> is_prime(1)
    False

    >>> is_prime(2)
    True

    >>> is_prime(3)
    True

    >>> is_prime(4)
    False

    >>> is_prime(7)
    True

    >>> is_prime(25)
    False
    """

    assert num >= 0, "Num should be a positive integer!"

    if num == 0 or num == 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False

    return True



def primes(count):
    """Return count number of prime numbers, starting at 2.

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

    """

    primes_list = []

    for i in range(100):
        if is_prime(i):
            primes_list.append(i)
    return primes_list[0:count]

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
