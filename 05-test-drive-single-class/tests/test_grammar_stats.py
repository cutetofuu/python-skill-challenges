import pytest
from lib.grammar_stats import *

"""
Given an empty string
#check raises an error
"""
def test_raises_error_for_empty_string():
    sentence = GrammarStats()
    with pytest.raises(Exception) as err:
        sentence.check("")
    error_message = str(err.value)
    assert error_message == "You have not entered a text."

"""
Given a text that starts with an uppercase word
and ends with a period
#check returns True
"""

def test_returns_true_for_uppercase_word_and_period():
    sentence = GrammarStats()
    assert sentence.check("Hello world.") == True

"""
Given a text that starts with an uppercase word
and ends with a semi-colon
#check returns False
"""
def test_returns_false_for_uppercase_word_and_semicolon():
    sentence = GrammarStats()
    assert sentence.check("Hello world;") == False

"""
Given a text that starts with a lowercase word
and ends with a period
#check returns False
"""
def test_returns_false_for_lowercase_word_and_period():
    sentence = GrammarStats()
    assert sentence.check("hello world.") == False

"""
Given a text that starts with an uppercase word
and ends with a period
#percentage_good returns 100
"""
def test_100_percent_for_one_correct_text():
    sentence = GrammarStats()
    sentence.check("Hello world.")
    assert sentence.percentage_good() == 100

"""
Given a text that starts with an uppercase word
and ends with a period
And a text that starts with an uppercase word
and ends with a semicolon
#percentage_good returns 50
"""
def test_50_percent_for_one_correct_text_and_one_wrong_text():
    sentence = GrammarStats()
    sentence.check("Hello world.")
    sentence.check("Hello world;")
    assert sentence.percentage_good() == 50

"""
Given a text that starts with an uppercase word
and ends with a period
And a text that starts with an uppercase word
and ends with a semicolon
And a text that starts with an lowercase word
and ends with an exclamation point
#percentage_good returns 33
"""
def test_33_percent_for_one_correct_text_and_two_wrong_texts():
    sentence = GrammarStats()
    sentence.check("Hello world.")
    sentence.check("Hello world;")
    sentence.check("hello world!")
    assert sentence.percentage_good() == 33

"""
Given a text that starts with an uppercase word
and ends with a period
And a text that starts with an uppercase word
and ends with a semicolon
And a text that starts with an uppercase word
and ends with an exclamation point
#percentage_good returns 67
"""

def test_67_percent_for_two_correct_texts_and_one_wrong_text():
    sentence = GrammarStats()
    sentence.check("Hello world.")
    sentence.check("Hello world;")
    sentence.check("Hello world!")
    assert sentence.percentage_good() == 67