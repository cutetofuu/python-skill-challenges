from lib.contacts import Contacts

"""
Initially returns an empty list
when no entries have been added yet
"""
def test_returns_empty_list_when_no_entries_added():
    contacts = Contacts()
    assert contacts.view_contacts_list() == []