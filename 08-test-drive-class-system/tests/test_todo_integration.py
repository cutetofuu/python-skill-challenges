import pytest
from lib.todo_list import TodoList
from lib.todo import Todo

"""
Given a value that's not an instance of the class #Todo
#add raises an error
"""
def test_raises_error_when_task_is_not_an_instance_of_todo_class():
    todo_list = TodoList()
    with pytest.raises(Exception) as err:
        todo_list.add("Wash the dishes")
    error_message = str(err.value)
    assert error_message == "This is not a proper todo task."

"""
Given a task
#incomplete returns a list with the todo task
"""
def test_incomplete_returns_list_with_a_task_given_one_task():
    todo_list = TodoList()
    task = Todo("Wash the dishes")
    todo_list.add(task)
    assert todo_list.incomplete() == [task]

"""
Given two tasks
#incomplete returns a list with the todo tasks
"""
def test_incomplete_returns_list_with_two_tasks_given_two_tasks():
    todo_list = TodoList()
    task_1 = Todo("Wash the dishes")
    task_2 = Todo("Mop the floor")
    todo_list.add(task_1)
    todo_list.add(task_2)
    assert todo_list.incomplete() == [task_1, task_2]

"""
Given a completed task
#complete returns a list with the completed task
#incomplete returns an empty list
"""
def test_complete_returns_list_with_a_task_given_one_completed_task():
    todo_list = TodoList()
    task = Todo("Wash the dishes")
    todo_list.add(task)
    task.mark_complete()
    assert todo_list.complete() == [task]
    assert todo_list.incomplete() == []

"""
Given five tasks
two complete and three incomplete
#complete returns a list with two tasks
#incomplete returns a list with three tasks
"""
def test_2_complete_tasks_3_incomplete_tasks_given_5_tasks():
    todo_list = TodoList()
    task_1 = Todo("Wash the dishes")
    task_2 = Todo("Mop the floor")
    task_3 = Todo("Complete the golden square challenges")
    task_4 = Todo("Jibble in")
    task_5 = Todo("Learn about class systems")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    todo_list.add(task_4)
    todo_list.add(task_5)
    task_2.mark_complete()
    task_5.mark_complete()
    assert todo_list.complete() == [task_2, task_5]
    assert todo_list.incomplete() == [task_1, task_3, task_4]


"""
Given five tasks
two complete and three incomplete
when #give_up is called
#complete returns a list with all the tasks
#incomplete returns an empty list
"""
def test_all_tasks_completed_when_give_up_called():
    todo_list = TodoList()
    task_1 = Todo("Wash the dishes")
    task_2 = Todo("Mop the floor")
    task_3 = Todo("Complete the golden square challenges")
    task_4 = Todo("Jibble in")
    task_5 = Todo("Learn about class systems")
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    todo_list.add(task_4)
    todo_list.add(task_5)
    task_2.mark_complete()
    task_5.mark_complete()
    todo_list.give_up()
    assert todo_list.complete() == [task_1, task_2, task_3, task_4, task_5]
    assert todo_list.incomplete() == []

