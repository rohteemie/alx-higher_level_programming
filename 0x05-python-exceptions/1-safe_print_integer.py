#!/usr/bin/python3


def safe_print_integer(value):
    i = 0
    try:
        i += value
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
