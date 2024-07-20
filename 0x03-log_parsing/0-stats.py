#!/usr/bin/python3

import sys


def print_msg(dict_sc, total_file_size):
    """
   The Method to print
    Args:
        dict_sc: dict of status codes
        total_file_size: variable total of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(total_file_size))
    for keyvar, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(keyvar, val))


total_file_size = 0
code = 0
counter = 0
dict_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # ✄ trimming
        parsed_line = parsed_line[::-1]  # inverting

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])  # the file size
                code = parsed_line[1]  # the status code

                if (code in dict_sc.keys()):
                    dict_sc[code] += 1

            if (counter == 10):
                print_msg(dict_sc, total_file_size)
                counter = 0

finally:
    print_msg(dict_sc, total_file_size)
