#!/usr/bin/python3
""" utf-8 validataion module
def validUTF8(data):
    :type data: List[int]
    rtype: bool
    count = 0
    for c in data:
        if count == 0:
            if (c >> 5) == 0b110:
                count = 1
            elif (c >> 4) == 0b1110:
                count = 2
            elif (c >> 3) == 0b11110:
                count = 3
            elif (c >> 7):
                return False
        else:
            if (c >> 6) != 0b10:
                return False
            count -= 1
    return count == 0
    """

from itertools import takewhile


NUMBER_OF_BITS_PER_BLOCK = 8
MAX_NUMBER_OF_ONES = 4


def to_bits(bytes):
    """ func to convert list of integers to bit"""
    for byte in bytes:
        num = []
        exp = 1 << NUMBER_OF_BITS_PER_BLOCK
        while exp:
            exp >>= 1
            num.append(bool(byte & exp))
        yield num


def validUTF8(data):
    """
    :type data: List[int]
    :rtype: bool
    """
    bits = to_bits(data)
    for byte in bits:
        # single byte char
        if byte[0] == 0:
            continue

        # multi-byte character
        amount = sum(takewhile(bool, byte))
        if amount <= 1:
            return False
        if amount >= MAX_NUMBER_OF_ONES:
            return False

        for _ in range(amount - 1):
            try:
                byte = next(bits)
            except StopIteration:
                return False
            if byte[0:2] != [1, 0]:
                return False
    return True
