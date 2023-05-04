from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
Given a diary entry
#read_entries returns a list with the diary entry
"""
def test_returns_list_with_1_entry_given_1_entry():
    diary = Diary()
    entry = DiaryEntry("Title 1", "Contents 1")
    diary.add(entry)
    assert diary.read_entries() == [entry]

"""
Given 3 diary entries
#read_entries returns a list
containing the 3 diary entries
"""
def test_returns_list_with_3_entries_given_3_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "Contents 1")
    entry_2 = DiaryEntry("Title 2", "Contents 2")
    entry_3 = DiaryEntry("Title 3", "Contents 3")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.read_entries() == [entry_1, entry_2, entry_3]

"""
Given 2 diary entries
and 2 wpm and 2 minutes
#select_best_entry_to_read returns the diary entry instance
closest to the length the user can read
"""
def test_returns_2nd_entry_given_2_wpm_2_mins_2_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "Contents 1")
    entry_2 = DiaryEntry("Title 2", "Hi there contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.select_best_entry_to_read(2, 2) == entry_2

"""
Given 3 diary entries, 
2 shorter and 1 longer
and given 3 wpm and 2 minutes
#select_best_entry_to_read returns the diary entry instance
closest to the length the user can read
"""
def test_returns_3rd_entry_given_3_wpm_2_mins_3_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "Contents 1")
    entry_2 = DiaryEntry("Title 2", "Hello and welcome again to contents 2")
    entry_3 = DiaryEntry("Title 3", "Hi there contents 3")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.select_best_entry_to_read(3, 2) == entry_3

"""
Given 3 diary entries, 
all longer than the length the user can read
and given 2 wpm and 3 minutes
#select_best_entry_to_read returns None
"""
def test_returns_none_given_2_wpm_3_mins_3_entries_too_long_to_read():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "Hi there, have you read about contents 1?")
    entry_2 = DiaryEntry("Title 2", "Hello and welcome again to contents 2")
    entry_3 = DiaryEntry("Title 3", "Goodbye and see you all tomorrow at contents 3")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.select_best_entry_to_read(2, 3) == None
