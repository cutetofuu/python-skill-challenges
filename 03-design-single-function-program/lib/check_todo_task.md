# Todo Function Design Recipe

## 1. Describe the Problem
_Put or write the user story here. Add any clarifying notes you might have._
> As a user

> So that I can keep track of my tasks

> I want to check if a text includes the string #TODO.

## 2. Design the Function Signature
_Include the name of the function, its parameters, return value, and side effects._
```python
def check_todo_task(string):
    # Checks if a text contains the string '#TODO'
    # Parameter: a string representing our task
    # Return: a boolean i.e. True or False
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests
_Make a list of examples of what the function will take and return._
```python
"""
Given a string that contains '#TODO' and the task
returns True
"""
check_todo_task("#TODO wash the dishes") => True

"""
Given a string that only contains '#TODO'
return False
"""
check_todo_task("#TODO") => False

"""
Given a string that contains '#todo'
returns False
"""
check_todo_task("#todo") => False

"""
Given a string that contains '#TO'
returns False
"""
check_todo_task("#TO") => False

"""
Given a string that doesn't contain '#TODO'
returns False
"""
check_todo_task("wash the dishes") => False

"""
Given a string that is empty ""
raises an Exception error
"""
check_todo_task("") => "You did not enter a task"

```
_Encode each example as a test. You can add to the above list as you go._
## 4. Implement the Behaviour
_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python
from lib.check_todo_task import *
"""
Given a string that contains '#TODO' and the task
returns True
"""
def test_check_todo_and_task():
    result = check_todo_task("#TODO wash the dishes")
    assert result == True
```
Ensure all test function names are unique, otherwise pytest will ignore them!