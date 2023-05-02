from lib.todo_list import TodoList

"""
#incomplete initially returns an empty list
when no todo tasks have been added
"""
def test_incomplete_list_returns_empty_list_when_no_tasks_added():
    todo_list = TodoList()
    assert todo_list.incomplete() == []

"""
#complete initially returns an empty list
when no todo tasks have been added
"""
def test_complete_list_returns_empty_list_when_no_tasks_added():
    todo_list = TodoList()
    assert todo_list.complete() == []