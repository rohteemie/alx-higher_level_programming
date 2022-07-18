#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        c = (fct(*args))
    except Exception as mssg:
        print("Exception: {}".format(mssg), file=sys.stderr)
        return None
    else:
        return c
