from lib.diary import Diary

"""
Initially returns an empty list
when no entries have been added
"""
def test_initially_returns_an_empty_list():
    diary = Diary()
    assert diary.all() == []