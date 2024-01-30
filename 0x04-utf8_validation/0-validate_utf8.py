#!/usr/bin/python3
"""method that determines if a given data set a valid UTF-8 encoding"""


def validUTF8(data):
    """method that determines if a given data set a valid UTF-8 encoding"""
    def start_byte(byte):
        return(byte & 0b10000000) == 0b00000000

    def continuation_byte(byte):
        return(byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        if 0 <= data[i] <= 255:
            if start_byte(data[i]):
                num = 1

                while num < 4 and \
                    i + num < len(data) and\
                        continuation_byte(data[i + num]):
                    num += 1

                if 1 <= num <= 4 and i + num <= len(data):
                    i += num
                else:
                    return False
            else:
                i += 1
        else:
            return False

    return True
