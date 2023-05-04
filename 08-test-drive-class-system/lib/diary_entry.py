import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("You haven't submitted a diary entry.")
        else:
            self.title = title
            self.contents = contents
        self._chunk_counter = 0

    def count_words(self):
        contents_words = self.contents.split()
        return len(contents_words)

    def reading_time(self, wpm):
        return math.ceil(len(self.contents.split()) / wpm)

    def reading_chunk(self, wpm, minutes):
        contents_words = self.contents.split()
        words_read = wpm * minutes

        start_index = 0 if self._chunk_counter == 0 else self._chunk_counter * words_read
        end_index = start_index + words_read

        contents_chunk = " ".join(contents_words[start_index:end_index])
        if len(contents_words[start_index:end_index]) == len(contents_words[start_index:]):
            self._chunk_counter = 0
        else:
            self._chunk_counter += 1

        return contents_chunk
        