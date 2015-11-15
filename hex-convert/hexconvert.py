def hex_convert(hex_in):
    """Convert a hexidecimal string, like '1A', into it's decimal equivalent.

        >>> hex_convert('6')
        6

        >>> hex_convert('10')
        16

        >>> hex_convert('FF')
        255

        >>> hex_convert('FFFF')
        65535
"""
    hex_dict = {'A':10,
                'B':11,
                'C':12,
                'D':13,
                'E':14,
                'F':15
                }

    hex_in_len = len(hex_in)
    decimal_value = 0
    # accounts for lowercase letters in hex_in
    hex_in = hex_in.upper()
    # adding 1s digit to decimal_value   
    if hex_in[-1].isalpha():
        decimal_value += hex_dict[hex_in[-1]]
    else:
        decimal_value += int(hex_in[-1])
    # adding rest of decimal place values to decimal_value
    for i in range(0, hex_in_len-1): # [0,1] 
        if hex_in[i].isalpha():
            decimal_value += hex_dict[hex_in[i]] * (16**(i+1))
        else:
            decimal_value += int(hex_in[i]) * (16**(i+1))
    print decimal_value

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. YOU'RE TERRIFIC!\n"
