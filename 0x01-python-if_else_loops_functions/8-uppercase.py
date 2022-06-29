#!/usr/bin/python3

# uppercase: Function that print a string in upercase
# sentence: variable holding converted character to ascii code
# strn: variable holding characters in loop from strings

def uppercase(str):
    for strn in range(len(str)):
        sentence = ord(str[strn])

        if (sentence >= 97 and sentence <= 122):
            sentence -= 32
        print("{:c}".format(sentence), end="")

    print()
