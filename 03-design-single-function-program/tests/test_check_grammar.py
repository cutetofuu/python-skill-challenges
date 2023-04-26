import pytest
from lib.check_grammar import *

"""
Given a string that starts with a lowercase letter
and no punctuation mark at the end
It returns False
"""
def test_checks_lowercase_with_no_punctuation():
    result = check_grammar("hello world")
    assert result == False

"""
Given a string that starts with an uppercase letter
but no punctuation mark at the end
It returns False
"""
def test_checks_uppercase_with_no_punctuation():
    result = check_grammar("Hello world")
    assert result == False

"""
Given a string that starts with a lowercase letter
with a punctuation mark at the end
It returns False
"""
def test_checks_lowercase_with_punctuation():
    result = check_grammar("hello world!")
    assert result == False

"""
Given a string that starts with an uppercase letter
but with an inappropriate punctuation mark at the end
It returns False
"""
def test_checks_uppercase_with_wrong_punctuation():
    result = check_grammar("Hello world;")
    assert result == False

"""
Given a string that starts with an uppercase word
and has an appropriate punctuation mark at the end
It returns True
"""
def test_checks_uppercase_with_correct_punctuation():
    result = check_grammar("Hello world!")
    assert result == True

"""
Given a string that has no words
but has a punctuation mark
It returns False
"""
def test_checks_no_words_with_punctuation():
    result = check_grammar("!")
    assert result == False

"""
Given an empty string
It raises an error
"""
def test_checks_string_raises_error():
    with pytest.raises(Exception) as e:
        check_grammar("")
    error_message = str(e.value)
    assert error_message == "The value cannot be empty."
