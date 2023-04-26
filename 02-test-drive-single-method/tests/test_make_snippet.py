from lib.make_snippet import *

def test_returns_empty_string():
    result = make_snippet("")
    assert result == ""

def test_with_less_than_5_words_returns_word():
    result = make_snippet("hello to you")
    assert result == "hello to you"

def test_with_exactly_5_words():
    result = make_snippet("harry potter the cursed child")
    assert result == "harry potter the cursed child"
    
def test_with_more_than_5_words():
    result = make_snippet("hello and welcome to the makers bootcamp")
    assert result == "hello and welcome to the..."