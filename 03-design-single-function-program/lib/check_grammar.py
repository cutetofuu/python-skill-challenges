def check_grammar(string):
    if string == "":
        raise Exception("The value cannot be empty.")
    elif string[0].isupper() and string[-1] in ".!?":
        return True
    return False
