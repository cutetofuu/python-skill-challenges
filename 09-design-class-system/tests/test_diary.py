from lib.diary import Diary

"""
Initially #read_entries returns an empty list
When no entries have been added yet
"""
def test_read_entries_initially_returns_empty_list():
    diary = Diary()
    assert diary.read_entries() == []

"""
Initially #select_best_entry_to_read returns None
Given 2 minutes and 2 wpm
But no entries have been added yet
"""
def test_select_best_entry_to_read_initially_returns_none():
    diary = Diary()
    assert diary.select_best_entry_to_read(2, 2) == None