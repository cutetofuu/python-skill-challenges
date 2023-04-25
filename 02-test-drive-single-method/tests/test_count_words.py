from lib.count_words import *

def test_returns_num_for_empty_string():
    result = count_words("")
    assert result == 1

"""
When passed a string with a whitespace
This will produce a list with two empty strings
and will return two
"""

def test_returns_num_for_empty_string_with_a_whitespace():
    result = count_words(" ")
    assert result == 2

def test_returns_num_for_one_word():
    result = count_words("hello")
    assert result == 1

def test_returns_num_for_multiple_words():
    result = count_words("hello world")
    assert result == 2