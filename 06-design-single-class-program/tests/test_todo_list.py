import pytest
from lib.todo_list import *

"""
Initially tells the user that
there are no tasks in this list
When no tasks have been added yet
"""
def test_returns_statement_when_no_tasks_given():
    todo = TodoList()
    assert todo.show_tasks() == "You don't have any saved tasks."

"""
Given a empty string as a task
#add_task raises an error
"""
def test_raises_error_when_empty_string_task_given():
    todo = TodoList()
    with pytest.raises(Exception) as err:
        todo.add_task("")
    error_message = str(err.value)
    assert error_message == "You have not set a task."

"""
Given a task
#show_tasks displays a list containing the task
"""
def test_given_one_task_returns_list_with_one_task():
    todo = TodoList()
    todo.add_task("Wash the dishes")
    assert todo.show_tasks() == "To Do List: Wash the dishes"

"""
Given two tasks
#show_tasks displays a list of both tasks
"""
def test_given_two_tasks_returns_list_with_two_tasks():
    todo = TodoList()
    todo.add_task("Wash the dishes")
    todo.add_task("Mop the floor")
    assert todo.show_tasks() == "To Do List: Wash the dishes, Mop the floor"

"""
Given two tasks
And marking off one the first task as complete
#show_tasks displays a list of containing only the second task
"""
def test_first_task_complete_only_returns_second_task():
    todo = TodoList()
    todo.add_task("Wash the dishes")
    todo.add_task("Mop the floor")
    todo.mark_task_as_complete("Wash the dishes")
    assert todo.show_tasks() == "To Do List: Mop the floor"

"""
Given four tasks
And marking off one the first and second tasks as complete
#show_tasks displays a list of containing 
only the third and fourth tasks
"""
def test_first_two_tasks_complete_only_returns_last_two_tasks():
    todo = TodoList()
    todo.add_task("Wash the dishes")
    todo.add_task("Mop the floor")
    todo.add_task("Have takeaway")
    todo.add_task("Cry deeply")
    todo.mark_task_as_complete("Wash the dishes")
    todo.mark_task_as_complete("Mop the floor")
    assert todo.show_tasks() == "To Do List: Have takeaway, Cry deeply"
