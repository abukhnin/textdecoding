# -*- coding: utf-8 -*-
'''
Module for text statistics calculation.
'''

import collections
import sys

# Temp

def get_char_frequencies(text):
    result = collections.defaultdict(int)
    for char in text:
        result[char] += 1
    return result

def main():
    print(get_char_frequencies(u"abc"))
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
