# Check Grammar Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user

> So that I can improve my grammar

> I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_grammar(string):
    """Checks if a text starts with a capital letter and ends with punctuation marks ".", "!" or "?"

    Parameters: (list all parameters and their types)
        text: a string containing words

    Returns: (state the return value and its type)
        a boolean value, either True or False

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string that starts with a lowercase letter
and no punctuation mark at the end
It returns False
"""
check_grammar("hello world") => False

"""
Given a string that starts with an uppercase letter
but no punctuation mark at the end
It returns False
"""
check_grammar("Hello world") => False

"""
Given a string that starts with a lowercase letter
with a punctuation mark at the end
It returns False
"""
check_grammar("hello world!") => False

"""
Given a string that starts with an uppercase letter
but with an inappropriate punctuation mark at the end
It returns False
"""
check_grammar("Hello world;") => False

"""
Given a string that has no words
but has an punctuation mark at the end
It returns False
"""
check_grammar("!") => False

"""
Given a string that starts with an uppercase word
and has an appropriate punctuation mark at the end
It returns True
"""
check_grammar("Hello world.") => True

"""
Given an empty string
It raises an exception
"""
check_grammar("") => "The value cannot be empty."

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.check_grammar import *

"""
Given a string that starts with a lowercase letter
and no punctuation mark at the end
It returns False
"""
def test_checks_lowercase_with_no_punctuation():
    result = check_grammar("hello")
    assert result == False

```

Ensure all test function names are unique, otherwise pytest will ignore them!