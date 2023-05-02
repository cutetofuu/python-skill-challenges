import math

class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        self._entries.append(entry)

    def all(self):
        return self._entries

    def count_words(self):
        total_word_count = 0
        for entry in self._entries:
            total_word_count += entry.count_words()
        return total_word_count

    def reading_time(self, wpm):
        return math.ceil(self.count_words() / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        best_entry = None
        
        for entry in self._entries:
            if best_entry == None and (len(entry.contents.split()) > wpm * minutes):
                continue
            elif best_entry == None and (len(entry.contents.split()) <= wpm * minutes):
                best_entry = entry
            elif ((len(entry.contents.split()) > len(best_entry.contents.split())) and (len(entry.contents.split()) <= wpm * minutes)):
                best_entry = entry

        if best_entry == None:
            return "All entries are over the available reading time."
        return best_entry
