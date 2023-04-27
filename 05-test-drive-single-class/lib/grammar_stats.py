class GrammarStats:
    def __init__(self):
        self._text_count = 0
        self._correct_text_count = 0

    def check(self, text):
        self._text_count += 1
        if text == "":
            raise Exception("You have not entered a text.")
        elif text[0].isupper() and text[-1] in ".!?":
            self._correct_text_count += 1
            return True
        return False

    def percentage_good(self):
        percentage = round((self._correct_text_count / self._text_count) * 100)
        return percentage