#!/usr/bin/python3
""" utf-8 validataion module """


def validUTF8(data):
    """:type data: List[int]
    rtype: bool"""
    numOfByte = 0
    for x in data:
        if numOfByte == 0:
            if (x >> 5) == 0b110 or x >> 5 == 0b1110:
                numOfByte = 1
            elif (x >> 4) == 0b1110:
                numOfByte = 2
            elif (x >> 3) == 0b11110:
                numOfByte = 3
            elif (x >> 7):
                return False
        else:
            if (x >> 6) != 0b10:
                return False
            numOfByte -= 1
    return numOfByte == 0
