import pytest
from lib.diary_entry import *

"""
Given empty title and contents
It raises an error
"""
def test_raises_error_for_empty_title_and_contents():
    with pytest.raises(Exception) as err:
        test_entry = DiaryEntry("", "")
    error_message = str(err.value)
    assert error_message == "You have not made a diary entry."

"""
Given a title and contents
It returns a formatted diary entry
"""
def test_returns_formatted_diary_entry():
    test_entry = DiaryEntry("Coding", "I love learning Python!")
    assert test_entry.format() == "Coding: I love learning Python!"

"""
Given a title and contents
It returns the number of words in the diary entry
"""
def test_counts_words_in_title_and_contents():
    test_entry = DiaryEntry("Coding", "I love learning Python!")
    assert test_entry.count_words() == 5

"""
Given a title, contents and the number of words a user can read per minute
It returns the estimated reading time in minutes for the contents
"""
def test_reading_time_four_mins_with_ten_wpm_and_36_words():
    test_entry = DiaryEntry(
        "I love My Kitty Cat Pickle", 
        "Eat half my food and ask for more use lap as chair. Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff."
    )
    assert test_entry.reading_time(10) == 4

"""
Given a title, contents, the number of words a user can read per minute
and the number of minutes the user has to read
It returns a chunk of the contents that the user was able to read
"""
def test_returns_first_contents_chunk():
    test_entry = DiaryEntry(
        "I love My Kitty Cat Pickle", 
        "Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff."
    )
    assert test_entry.reading_chunk(10, 1) == "Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching"

"""
Given a title and contents
Then given the number of words a user can read per minute 
and the number of minutes the user has to read twice
It returns the second chunk of the contents that the user was able to read
"""
def test_returns_second_contents_chunk():
    test_entry = DiaryEntry(
        "I love My Kitty Cat Pickle", 
        "Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff."
    )
    test_entry.reading_chunk(10, 1)
    assert test_entry.reading_chunk(10, 1) == "attack your ankles chase the red dot, hairball run catnip"

"""
Given a title and contents
Then given the number of words a user can read per minute 
and the number of minutes the user has to read multiple times
until the end of the contents has been reached
It returns the last chunk of the contents
"""

def test_returns_last_contents_chunk():
    test_entry = DiaryEntry(
        "I love My Kitty Cat Pickle", 
        "Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff."
    )
    test_entry.reading_chunk(10, 1)
    test_entry.reading_chunk(10, 1)
    assert test_entry.reading_chunk(10, 1) == "eat the grass sniff."

"""
1. Given a title and contents
2. Given the number of words a user can read per minute 
and the number of minutes the user has to read multiple times
until the end of the contents has been reached
3. Then once again, given the number of words a user can read per minute
and the number of minutes the user has to read multiple times
It returns the first chunk of the contents that the user was able to read
"""

def test_resets_contents_chunk_and_returns_first_chunk():
    test_entry = DiaryEntry(
        "I love My Kitty Cat Pickle", 
        "Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff."
    )
    test_entry.reading_chunk(10, 1)
    test_entry.reading_chunk(10, 1)
    test_entry.reading_chunk(10, 1)
    assert test_entry.reading_chunk(10, 1) == "Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching"