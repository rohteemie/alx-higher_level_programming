#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    error = "Exception: "
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as mssg:
        error += str(mssg)
        error += '\n'
        sys.stderr.write(error)
        return False
