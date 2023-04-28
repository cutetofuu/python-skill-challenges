# To Do List Class Design Recipe

## 1. Describe the Problem

> As a user  
> So that I can keep track of my tasks
> I want a program that I can add todo tasks to and see a list of them.

> As a user  
> So that I can focus on tasks to complete  
> I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class TodoList():
    def __init__(self):
        # Parameters:
        #   none
        # States:
        #   todo_list: an empty list
        # Side effects:
        #   none
        pass # No code here yet

    def add_task(self, task):
        # Parameters:
        #   task: string
        # Side effects:
        #   Appends the #task string to the #self.todo_list list
        #   Throws an error if no task is set
        pass # No code here yet

    def show_tasks(self):
        # Parameters:
        #   none
        # Side effects:
        #   none
        pass # No code here yet

    def mark_task_as_complete(self, task):
        # Parameters:
        #   task: string
        # Side effects:
        #   Removes the #task from the #self.todo_list list
        pass # No code here yet

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Initially tells the user that
there are no tasks in this list
When no tasks have been added yet
"""
todo = TodoList()
todo.show_tasks() => "You don't have any saved tasks."

"""
Given a empty string as a task
#add_task raises an error
"""
todo = TodoList()
todo.add_task("") # raises an error with the message
"You have not set a task."

"""
Given a task
#show_tasks displays a list containing the task
"""
todo = TodoList()
todo.add_task("Wash the dishes")
todo.show_tasks() => "To Do List: Wash the dishes"

"""
Given two tasks
#show_tasks displays a list of both tasks
"""
todo = TodoList()
todo.add_task("Wash the dishes")
todo.add_task("Mop the floor")
todo.show_tasks() => "To Do List: Wash the dishes, Mop the floor"

"""
Given two tasks
And marking off one the first task as complete
#show_tasks displays a list of containing only the second task
"""
todo = TodoList()
todo.add_task("Wash the dishes")
todo.add_task("Mop the floor")
todo.mark_task_as_complete("Wash the dishes")
todo.show_tasks() => "To Do List: Mop the floor"

"""
Given four tasks
And marking off one the first and second tasks as complete
#show_tasks displays a list of containing 
only the third and fourth tasks
"""
todo = TodoList()
todo.add_task("Wash the dishes")
todo.add_task("Mop the floor")
todo.add_task("Have takeaway")
todo.add_task("Cry deeply")
todo.mark_task_as_complete("Wash the dishes")
todo.mark_task_as_complete("Mop the floor")
todo.show_tasks() => "To Do List: Have takeaway, Cry deeply"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
