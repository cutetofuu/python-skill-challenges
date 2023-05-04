class Todo:
    def __init__(self, todo):
        if todo == "":
            raise Exception("You have not entered a task.")
        else:
            self.todo = todo
            self.complete = False

    def mark_complete(self):
        self.complete = True