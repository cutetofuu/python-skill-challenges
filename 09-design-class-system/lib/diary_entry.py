class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("You haven't submitted a diary entry.")
        else:
            self.title = title
            self.contents = contents
