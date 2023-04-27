import pytest
from lib.check_todo_task import *

"""
Given a string that contains '#TODO' and the task 
returns True
"""
def test_check_todo_and_task():
    result = check_todo_task("#TODO wash the dishes")
    assert result == True

"""
Given a string that only contains '#TODO'
return False
"""
def test_check_only_todo():
    result = check_todo_task("#TODO")
    assert result == False 

"""
Given a string that contains lowercase '#todo'
returns False
"""
def test_check_lowercase_todo():
    result = check_todo_task("#todo wash the dishes")
    assert result == False

"""
Given a string that contains '#TO'
returns False
"""
def test_check_incomplete_todo():
    result = check_todo_task("#TO wash the dishes")
    assert result == False

"""
Given a string that doesn't contain '#TODO'
returns False
"""
def test_check_without_todo():
    result = check_todo_task("wash the dishes")
    assert result == False

"""
Given a string that is empty ""
raises an Exception error
"""
def test_check_empty_string_throws_error():
    with pytest.raises(Exception) as err:
        check_todo_task("")
    error_message = str(err.value)
    assert error_message == "You did not specify a task"