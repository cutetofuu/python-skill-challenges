from lib.todo_list import TodoList

"""
#incomplete_tasks initially returns an empty list
when no todo tasks have been added
"""
def test_incomplete_returns_empty_list_when_no_tasks_added():
    todo_list = TodoList()
    assert todo_list.incomplete_tasks() == []

"""
#complete_tasks initially returns an empty list
when no todo tasks have been added
"""
def test_complete_returns_empty_list_when_no_tasks_added():
    todo_list = TodoList()
    assert todo_list.complete_tasks() == []