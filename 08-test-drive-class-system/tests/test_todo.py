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
and state of whether it's been completed
"""
def test_returns_task_and_completed_status():
    task = Todo("Wash the dishes")
    assert task.task == "Wash the dishes"
    assert task.complete == False

"""
When a task has been created
#mark_complete changes the complete state to True
"""
def test_mark_complete_changes_completed_status_to_true():
    task = Todo("Wash the dishes")
    task.mark_complete()
    assert task.complete == True