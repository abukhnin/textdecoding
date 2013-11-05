# -*- coding: utf-8 -*-
'''
Module for text decoding.
'''

import textstatistics

def encode_text(text, code):
    '''
    Encodes the text with a substitution cipher defined with the code.
    Argument "code" is a dictionary with characters as keys 
    and corresponding coding characters as values. 
    For example:
        code = { 'a': 'z', 'b': 'y' , 'c': 'x' }
    '''
    return ''

def evalutate_decoding(text, language):
    '''
    Evaluates how the decoded text corresponds to the language.
    Returns estimated fitness as a float value from the range [0; 1], where
    0 means doesn't correspond at all,
    1 means all words are correct.
    '''
    fitness_sum = 0.0
    words = textstatistics.split_to_words(text)
    for word in words:
        fitness_sum += language.word_fitness(word)
    return fitness_sum / len(words)

def decode_text(text, language):
    '''
    Decodes the text encoded with a substitution cipher
    '''
    return ''
