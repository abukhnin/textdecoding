# -*- coding: utf-8 -*-
'''
Tests for decode module
'''

import unittest
import os
import sys
import random

root_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
sys.path.append(root_path)

import decode
import textstatistics
from test import data


class TestDecodeText(unittest.TestCase):
    def test_decode_text_same_rus(self):
        original_alphabet = list(u'абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        shuffled_alphabet = list(original_alphabet)
        random.seed(1001)
        random.shuffle(shuffled_alphabet)

        code = dict(zip(original_alphabet, shuffled_alphabet))

        original_text = data.QUOTE_FROM_ILF_AND_PETROV
        encoded_text = decode.encode_text(original_text, code)
        print 'TestDecodeText::encoded_text:', encoded_text

        alphabet = textstatistics.get_char_frequencies(original_text)
        dictionary = textstatistics.get_word_frequencies(original_text)
        language = textstatistics.Languauge(alphabet, dictionary)

        decoded_text = decode.decode_text(encoded_text, language)
        self.assertEqual(original_text, decoded_text)


class TestEvalutateDecoding(unittest.TestCase):
    def test_evalutate_decoding_complete_eng(self):
        decoded_text = base_text = 'This is a sample text.'

        alphabet = textstatistics.get_char_frequencies(base_text)
        dictionary = textstatistics.get_word_frequencies(base_text)
        language = textstatistics.Languauge(alphabet, dictionary)

        result = decode.evalutate_decoding(decoded_text, language)
        self.assertEqual(result, 1.0)

    def test_evalutate_decoding_subset_eng(self):
        base_text = 'This is a sample text.'
        base_text_words = textstatistics.split_to_words(base_text)
        decoded_text = ' '.join(base_text_words[: len(base_text_words) / 2])

        alphabet = textstatistics.get_char_frequencies(base_text)
        dictionary = textstatistics.get_word_frequencies(base_text)
        language = textstatistics.Languauge(alphabet, dictionary)

        result = decode.evalutate_decoding(decoded_text, language)
        self.assertEqual(result, 1.0)

    def test_evalutate_decoding_almost_eng(self):
        base_text = 'This is a sample text.'
        decoded_text = 'Thas as i simple text.'

        alphabet = textstatistics.get_char_frequencies(base_text)
        dictionary = textstatistics.get_word_frequencies(base_text)
        language = textstatistics.Languauge(alphabet, dictionary)

        result = decode.evalutate_decoding(decoded_text, language)
        self.assertTrue(result < 1.0 and result > 0.5)


if __name__ == "__main__":
    unittest.main()
