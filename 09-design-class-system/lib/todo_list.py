class TodoList:
    def __init__(self):
        self._todo_list = []

    def add(self, task):
        self._todo_list.append(task)

    def incomplete_tasks(self):
        return [task for task in self._todo_list if task.complete == False]

    def complete_tasks(self):
        return [task for task in self._todo_list if task.complete == True]
