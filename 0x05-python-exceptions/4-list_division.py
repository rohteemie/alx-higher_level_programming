#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    c = 0
    new_list = []
    for i in range(list_length):
        try:
            c = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(c)
            c = 0
    return new_list
