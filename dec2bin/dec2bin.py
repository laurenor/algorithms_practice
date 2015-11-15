def dec2bin(num):
    from math import log
    """Convert a decimal number to binary representation.

    >>> dec2bin(0)
    '0'

    >>> dec2bin(1)
    '1'

    >>> dec2bin(2)
    '10'

    >>> dec2bin(4)
    '100'

    >>> dec2bin(15)
    '1111'
    """
    # multiples of 2
    if log(num) % log(2) == 0:
        return str(int(log(num)/log(2)))
    elif num % 2 != 0:
        # odd numbers
        return dec2bin(num) + 1 
    else:
        # numbers divisible by 2, but not powers of 2
        count = 0
        result = num
        while result > 1:
            result /= 2
            count += 1
        remainder = num - 2**count
        return 10**count + dec2bin(remainder)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
