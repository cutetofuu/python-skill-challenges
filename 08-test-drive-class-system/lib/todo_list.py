from lib.todo import Todo

class TodoList:
    def __init__(self):
        self._todo_list = []

    def add(self, todo):
        if isinstance(todo, Todo):
            self._todo_list.append(todo)
        else:
            raise Exception("This is not a proper todo task.")
    
    def incomplete(self):
        incomplete_list = list(filter(lambda task: task.complete == False, self._todo_list))
        return incomplete_list

    def complete(self):
        complete_list = list(filter(lambda task: task.complete == True, self._todo_list))
        return complete_list

    def give_up(self):
        for task in self._todo_list:
            task.mark_complete()
