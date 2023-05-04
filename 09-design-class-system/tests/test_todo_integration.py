from lib.todo_list import TodoList
from lib.todo import Todo

"""
Given a task
#incomplete_tasks returns a list with the task
"""
def test_incomplete_returns_list_with_1_task_given_1_task():
    todo_list = TodoList()
    task = Todo("Walk the cat")
    todo_list.add(task)
    assert todo_list.incomplete_tasks() == [task]

"""
Given three tasks
#incomplete_tasks returns a list with three tasks
"""
def test_incomplete_returns_list_with_3_tasks_given_3_tasks():
    todo_list = TodoList()
    task_1 = Todo("Walk the cat")
    task_2 = Todo("Mop the floor")
    task_3 = Todo("Wash the dishes")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    assert todo_list.incomplete_tasks() == [task_1, task_2, task_3]

"""
Given a completed task
#complete_tasks returns a list with the completed task
#incomplete_tasks returns an empty list
"""
def test_complete_returns_list_with_1_task_given_1_completed_task():
    todo_list = TodoList()
    task = Todo("Wash the dishes")
    todo_list.add(task)
    task.mark_complete()
    assert todo_list.complete_tasks() == [task]
    assert todo_list.incomplete_tasks() == []

"""
Given four tasks
three complete and one incomplete
#complete_tasks returns a list with three tasks
"""
def test_complete_returns_3_tasks_given_4_tasks():
    todo_list = TodoList()
    task_1 = Todo("Wash the dishes")
    task_2 = Todo("Mop the floor")
    task_3 = Todo("Complete the golden square challenges")
    task_4 = Todo("Jibble in")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    todo_list.add(task_4)
    task_1.mark_complete()
    task_2.mark_complete()
    task_4.mark_complete()
    assert todo_list.complete_tasks() == [task_1, task_2, task_4]

"""
Given four tasks
two complete and two incomplete
#incomplete_tasks returns a list with two tasks
"""
def test_incomplete_returns_2_tasks_given_4_tasks():
    todo_list = TodoList()
    task_1 = Todo("Wash the dishes")
    task_2 = Todo("Mop the floor")
    task_3 = Todo("Complete the golden square challenges")
    task_4 = Todo("Jibble in")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    todo_list.add(task_4)
    task_2.mark_complete()
    task_4.mark_complete()
    assert todo_list.incomplete_tasks() == [task_1, task_3]