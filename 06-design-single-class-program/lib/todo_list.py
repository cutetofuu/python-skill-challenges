class TodoList():
    def __init__(self):
        self._todo_list = []

    def add_task(self, task):
        if task == "":
            raise Exception("You have not set a task.")
        else:
            self._todo_list.append(task)

    def show_tasks(self):
        if self._todo_list == []:
            return "You don't have any saved tasks."
        else:
            tasks_string = ", ".join(self._todo_list)
            return f"To Do List: {tasks_string}"

    def mark_task_as_complete(self, task):
        self._todo_list.remove(task)