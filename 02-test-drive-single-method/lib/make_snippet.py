def make_snippet(string):
    phrase_split = string.split(" ")
    
    if len(phrase_split) > 5:
        new_phrase = " ".join(phrase_split[:5])  + "..."
        return new_phrase

    return string