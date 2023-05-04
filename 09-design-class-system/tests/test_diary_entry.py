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
Returns the entry's title
"""
def test_returns_title_and_contents_when_entry_created():
    entry = DiaryEntry("Title 1", "Contents 1")
    assert entry.title == "Title 1"

"""
When an entry has been created
Returns the entry's contents
"""
def test_returns_title_and_contents_when_entry_created():
    entry = DiaryEntry("Title 1", "Contents 1")
    assert entry.contents == "Contents 1"
