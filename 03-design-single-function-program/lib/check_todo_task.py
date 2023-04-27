def check_todo_task(string):
    if string == "":
        raise Exception("You did not specify a task")
    elif "#TODO" in string and len(string) > 5:
        return True
    return False