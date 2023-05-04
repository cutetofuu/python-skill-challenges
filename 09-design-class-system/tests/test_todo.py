import pytest
from lib.todo import Todo

"""
Given an empty string
It returns an error
"""
def test_raises_error_given_an_empty_string():
    with pytest.raises(Exception) as err:
        task = Todo("")
    error_message = str(err.value)
    assert error_message == "You have not entered a task."

"""
When a task has been created
Returns the task itself 
"""
def test_returns_task_given_a_task():
    task = Todo("Wash the dishes")
    assert task.todo == "Wash the dishes"

"""
When a task has been created
Returns a complete state of False
"""
def test_returns_complete_state_of_false_given_a_task():
    task = Todo("Wash the dishes")
    assert task.complete == False

"""
When a task has been created
#mark_complete changes the complete state to True
"""
def test_mark_complete_changes_complete_state_to_true():
    task = Todo("Wash the dishes")
    task.mark_complete()
    assert task.complete == True