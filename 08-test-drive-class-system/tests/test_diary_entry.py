import pytest
from lib.diary_entry import DiaryEntry

"""
Given an empty string for title and contents
Raises an error
"""
def test_raises_error_given_empty_string():
    with pytest.raises(Exception) as err:
        entry = DiaryEntry("", "")
    error_message = str(err.value)
    assert error_message == "You haven't submitted a diary entry."

"""
When an entry has been created
Returns the entry's title and contents
"""
def test_returns_title_and_contents_when_entry_created():
    entry = DiaryEntry("Title 1", "Contents 1")
    assert entry.title == "Title 1"
    assert entry.contents == "Contents 1"

"""
When an entry has been created
#count_words returns the number of words in the contents
"""
def test_returns_contents_word_count_when_entry_created():
    entry = DiaryEntry("Title 1", "Contents 1")
    assert entry.count_words() == 2

"""
When an entry has been created with 6 words
and given 3 wpm
#reading_time returns a reading time of 2 minutes
with the value being an integer
"""
def test_returns_2_mins_given_3_wpm_and_6_words():
    entry = DiaryEntry("Title 1", "Hi there and welcome contents 1")
    assert entry.reading_time(3) == 2
    assert type(entry.reading_time(3)) == int

"""
When an entry has been created with 11 words
and given 4 wpm
#reading_time returns a reading time of 3 minutes
with the value being an integer
"""
def test_returns_3_mins_given_4_wpm_and_1_words():
    entry = DiaryEntry("Title 1", "Hi there and welcome to contents 1! This is an entry.")
    assert entry.reading_time(4) == 3
    assert type(entry.reading_time(3)) == int

"""
Given an entry, 2 wpm
and an available reading time of 2 minutes
#reading_chunk returns the first chunk of the contents 
that the user was able to read
"""
def test_returns_first_contents_chunk():
    entry = DiaryEntry("Title 1", "Hi there and welcome to Makers! This is a diary entry.")
    assert entry.reading_chunk(2, 2) == "Hi there and welcome"

"""
Given an entry, 2 wpm
and an available reading time of 2 minutes
#reading_chunk called out twice
returns the second chunk of the contents 
that the user was able to read
"""
def test_returns_second_contents_chunk():
    entry = DiaryEntry("Title 1", "Hi there and welcome to Makers! This is a diary entry.")
    entry.reading_chunk(2, 2)
    assert entry.reading_chunk(2, 2) == "to Makers! This is"

"""
Given an entry, 2 wpm
and an available reading time of 2 minutes
#reading_chunk called out three times
returns the last chunk of the contents 
that the user was able to read
"""
def test_returns_last_contents_chunk():
    entry = DiaryEntry("Title 1", "Hi there and welcome to Makers! This is a diary entry.")
    entry.reading_chunk(2, 2)
    entry.reading_chunk(2, 2)
    assert entry.reading_chunk(2, 2) == "a diary entry."

"""
Given an entry, 2 wpm
and an available reading time of 2 minutes
#reading_chunk called out four times
goes back to the beginning
and returns the first chunk of the contents 
that the user was able to read
"""
def test_chunk_resets_and_returns_first_contents_chunk():
    entry = DiaryEntry("Title 1", "Hi there and welcome to Makers! This is a diary entry.")
    entry.reading_chunk(2, 2)
    entry.reading_chunk(2, 2)
    entry.reading_chunk(2, 2)
    assert entry.reading_chunk(2, 2) == "Hi there and welcome"

"""
Given an entry with 12 words, 2 wpm
and an available reading time of 2 minutes
#reading_chunk called out four times
goes back to the beginning
and returns the first chunk of the contents 
that the user was able to read
"""
def test_chunk_resets_and_returns_first_contents_chunk_given_12_words():
    entry = DiaryEntry("Title 1", "Hi there and welcome to Makers! This is yet another diary entry.")
    entry.reading_chunk(2, 2)
    entry.reading_chunk(2, 2)
    entry.reading_chunk(2, 2)
    assert entry.reading_chunk(2, 2) == "Hi there and welcome"