# -*- coding: utf-8 -*-
'''
Module for text statistics calculation.
'''

import sys

def get_char_frequencies(text):
    result = {}
    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def main():
    print(get_char_frequencies(u"abc"))
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
