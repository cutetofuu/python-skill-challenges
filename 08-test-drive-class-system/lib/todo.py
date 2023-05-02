class Todo:
    def __init__(self, task):
        if task == "":
            raise Exception("You have not entered a task.")
        else:
            self.task = task
            self.complete = False

    def mark_complete(self):
        self.complete = True