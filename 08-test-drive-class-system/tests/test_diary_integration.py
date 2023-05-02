from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
Given a diary entry
#all returns a list with the diary entry
"""
def test_returns_list_with_an_entry_given_one_entry():
    diary = Diary()
    entry = DiaryEntry("Title 1", "Contents 1")
    diary.add(entry)
    assert diary.all() == [entry]

"""
Given two diary entries
#all returns a list with the diary entry
"""
def test_returns_list_with_two_entries_given_two_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "Contents 1")
    entry_2 = DiaryEntry("Title 2", "Contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

"""
Given a diary entry
#count_words returns the number of words in the entry
"""
def test_returns_word_count_given_one_entry():
    diary = Diary()
    entry = DiaryEntry("Title 1", "Contents 1")
    diary.add(entry)
    assert diary.count_words() == 2

"""
Given two diary entries
#count_words returns the number of words in the entry
"""
def test_returns_total_word_count_given_two_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "Contents 1")
    entry_2 = DiaryEntry("Title 2", "This is contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 6

"""
Given two diary entries with 6 words and 2 wpm
#reading_time returns the reading time of 3 minutes
as an integer value
"""
def test_returns_3_mins_given_2_wpm_and_2_entries_with_6_words():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "Contents 1")
    entry_2 = DiaryEntry("Title 2", "This is contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 3
    assert type(diary.reading_time(2)) == int

"""
Given three diary entries with 10 words and 3wpm
#reading_time returns the reading time of 4 minutes
as an integer value
"""
def test_returns_3_mins_given_2_wpm_and_2_entries_with_6_words():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "Hello contents 1")
    entry_2 = DiaryEntry("Title 2", "This is contents 2")
    entry_3 = DiaryEntry("Title 2", "Goodbye contents 3")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.reading_time(3) == 4
    assert type(diary.reading_time(3)) == int

"""
Given two diary entries, 4 wpm and 1 minute
#find_best_entry_for_reading_time returns the diary entry instance
closest to the length the user can read
"""
def test_returns_2nd_entry_given_4_wpm_1_min_and_2_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "Hello contents 1")
    entry_2 = DiaryEntry("Title 2", "This is contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(4, 1) == entry_2

"""
Given three diary entries, 3 wpm and 2 minutes
#find_best_entry_for_reading_time returns the diary entry instance
closest to the length the user can read
"""
def test_returns_3rd_entry_given_3_wpm_2_mins_and_3_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "Hello there and welcome to contents 1")
    entry_2 = DiaryEntry("Title 2", "Hi there contents 2")
    entry_3 = DiaryEntry("Title 2", "Goodbye and thank you contents 3")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.find_best_entry_for_reading_time(3, 2) == entry_3

"""
Given three diary entries 
with all entries over the length
that the user can read in a minute
and given 3 wpm and 1 minute
#find_best_entry_for_reading_time returns the diary entry instance
closest to the length the user can read
"""
def test_returns_none_given_3_wpm_1_min_and_3_lengthy_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "Hello there contents 1")
    entry_2 = DiaryEntry("Title 2", "Contents 2 lives here")
    entry_3 = DiaryEntry("Title 2", "Goodbye and thank you contents 3")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.find_best_entry_for_reading_time(3, 1) == "All entries are over the available reading time."
