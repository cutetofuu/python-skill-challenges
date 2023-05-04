import re

class Contacts:
    def __init__(self):
        self._contacts_list = []

    def add_number(self, entry):
        title_mobile_nums = re.findall("(07\\d{9}|\\+447\\d{9}|00447\\d{9})", entry.title)
        contents_mobile_nums = re.findall("(07\\d{9}|\\+447\\d{9}|00447\\d{9})", entry.contents)

        if title_mobile_nums != []:
            self._contacts_list.extend(title_mobile_nums)

        if contents_mobile_nums != []:
            self._contacts_list.extend(contents_mobile_nums)

    def view_contacts_list(self):
        return self._contacts_list