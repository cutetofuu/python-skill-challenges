class Diary:
    def __init__(self):
        self._entries_list = []

    def add(self, entry):
        self._entries_list.append(entry)

    def read_entries(self):
        return self._entries_list

    def select_best_entry_to_read(self, minutes, wpm):
        best_entry = None
        words_user_can_read = wpm * minutes
        
        for entry in self._entries_list:
            count_words = len(entry.contents.split())

            if best_entry == None and (count_words > words_user_can_read):
                continue
            elif best_entry == None and (count_words <= words_user_can_read):
                best_entry = entry
            elif ((count_words > len(best_entry.contents.split())) and (count_words <= words_user_can_read)):
                best_entry = entry

        return best_entry