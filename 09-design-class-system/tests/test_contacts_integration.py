from lib.contacts import Contacts
from lib.diary_entry import DiaryEntry

"""
Given 1 diary entry with no mobile numbers
Returns an empty list
"""
def test_returns_empty_list_given_1_entry_with_no_numbers():
    contacts = Contacts()
    entry = DiaryEntry("Title 1", "Contents 1")
    contacts.add_number(entry)
    assert contacts.view_contacts_list() == []

"""
Given 3 diary entries with no mobile numbers
Returns an empty list
"""
def test_returns_empty_list_given_3_entries_with_no_numbers():
    contacts = Contacts()
    entry_1 = DiaryEntry("Title 1", "Contents 1")
    entry_2 = DiaryEntry("Title 5", "Contents 7")
    entry_3 = DiaryEntry("Title 3", "Contents 9")
    contacts.add_number(entry_1)
    contacts.add_number(entry_2)
    contacts.add_number(entry_3)
    assert contacts.view_contacts_list() == []

"""
Given 1 diary entry with a mobile number 
in 07xxx-xxx-xxxx format
Returns a list with 1 mobile number
"""

def test_returns_1_number_given_entry_with_07_number():
    contacts = Contacts()
    entry = DiaryEntry("Title 1", "Here's my friend's number: 07777888888")
    contacts.add_number(entry)
    assert contacts.view_contacts_list() == ["07777888888"]

"""
Given 1 diary entry with a mobile number 
in +447xxx-xxx-xxxx format
Returns a list with 1 mobile number
"""
def test_returns_1_number_given_entry_with_447_number():
    contacts = Contacts()
    entry = DiaryEntry("Title 1", "+447777888888 is my friend's number")
    contacts.add_number(entry)
    assert contacts.view_contacts_list() == ["+447777888888"]

"""
Given 1 diary entry with a mobile number 
in 00447xxx-xxx-xxxx format
Returns a list with 1 mobile number
"""
def test_returns_1_number_given_entry_with_00447_number():
    contacts = Contacts()
    entry = DiaryEntry("A friend's number of 00447777888888", "This is my friend's number")
    contacts.add_number(entry)
    assert contacts.view_contacts_list() == ["00447777888888"]

"""
Given 3 diary entries with 4 mobile numbers
in 07xxx-xxx-xxxx, +447xxx-xxx-xxxx and 00447xxx-xxx-xxxx formats
Returns a list with 3 mobile numbers
"""
def test_returns_3_numbers_given_2_entries_with_07_numbers():
    contacts = Contacts()
    entry_1 = DiaryEntry("A friend's number of 07777888888", "Contents 1")
    entry_2 = DiaryEntry("Title 2", "One of my coworkers can be contacted at 07444666666")
    entry_3 = DiaryEntry("Title 3", "It's at +447555777777 or 00447999999999 that the electrician can be phoned on")
    contacts.add_number(entry_1)
    contacts.add_number(entry_2)
    contacts.add_number(entry_3)
    assert contacts.view_contacts_list() == ["07777888888", "07444666666", "+447555777777", "00447999999999"]
