import pytest
from lib.diary import Diary

"""
Initially returns an empty list
when no entries have been added
"""
def test_initially_returns_an_empty_list():
    diary = Diary()
    assert diary.all() == []

"""
Initially has a word count of 0
when no entries have been added
"""
def test_initially_returns_zero_word_count():
    diary = Diary()
    assert diary.count_words() == 0

"""
Initially #reading_time should raise an error
"""
def test_reading_time_initially_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.reading_time(2)
    error_message = str(err.value)
    assert error_message == "No entries have been added yet."

"""
Initially #find_best_entry_for_reading_time should raise an error
"""
def test_best_entry_for_reading_time_initially_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.find_best_entry_for_reading_time(2, 2)
    error_message = str(err.value)
    assert error_message == "No entries have been added yet."