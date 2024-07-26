#!/usr/bin/python3
""" UTF-8 Validation"""


def validUTF8(data):
    """FUnction determines if a given data is set
       represents a valid utf-8 encoding
    """
    num_bytesvr = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:

        mask_bytevr = 1 << 7

        if num_bytesvr == 0:

            while mask_bytevr & i:
                num_bytesvr += 1
                mask_bytevr = mask_bytevr >> 1

            if num_bytesvr == 0:
                continue

            if num_bytesvr == 1 or num_bytesvr > 4:
                return False

        else:
            if not (i & mask_1 and not (i & mask_2)):
                return False

        num_bytesvr -= 1

    if num_bytesvr == 0:
        return True

    return False
