import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("You have not made a diary entry.")
        else:
            self.title = title
            self.contents = contents
            self.chunk_counter = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        title_word_count = len(self.title.split(" "))
        contents_word_count = len(self.contents.split(" "))
        return title_word_count + contents_word_count

    def reading_time(self, wpm):
        contents_word_count = len(self.contents.split(" "))
        return math.ceil(contents_word_count / wpm)

    def reading_chunk(self, wpm, minutes):
        contents_words = self.contents.split(" ")
        words_read = wpm * minutes

        start_index = 0 if self.chunk_counter == 0 else self.chunk_counter * words_read
        end_index = start_index + words_read

        contents_chunk = " ".join(contents_words[start_index:end_index])
        if len(contents_words[start_index:end_index]) == len(contents_words[start_index:]):
            self.chunk_counter = 0
        else:
            self.chunk_counter += 1

        return contents_chunk