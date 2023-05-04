# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

> As a user  
> So that I can record my experiences  
> I want to keep a regular diary

> As a user  
> So that I can reflect on my experiences  
> I want to read my past diary entries 

> As a user  
> So that I can reflect on my experiences in my busy day  
> I want to select diary entries to read based on how much time I have and my
> reading speed

> As a user  
> So that I can keep track of my tasks  
> I want to keep a todo list along with my diary

> As a user  
> So that I can keep track of my contacts  
> I want to see a list of all of the mobile phone numbers in all my diary
> entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
# Nouns
experiences
diary
diary entries
how much time I have
my reading speed
todo list
contacts
list of all mobile phone numbers

# Verbs
record experiences
read past entries
select entries to read
keep a todo list
see a list of mobile numbers


  ┌───────────────────────────────────────────┐
  │ Diary                                     │
  │                                           │
  │ - add(entry)                              │
  │ - read_entries()                          │
  │ - select_best_entry_to_read(minutes, wpm) │
  └────────────────────┬──────────────────────┘
                       │
                       │  owns a list of
                       │
  ┌────────────────────▼──────────────────────┐
  │ DiaryEntry                                │
  │                                           │
  │ - title                                   │
  │ - contents                                │
  └───────────────────────────────────────────┘

  ┌───────────────────────────────────────────┐
  │ TodoList                                  │
  │                                           │
  │ - add(task)                               │
  │ - incomplete_tasks()                      │
  │ - complete_tasks()                        │
  └─────────────────────┬─────────────────────┘
                        │
                        │ owns a list of
                        │
  ┌─────────────────────▼─────────────────────┐
  │ Todo                                      │
  │                                           │
  │ - initialize(task)                        │
  │ - mark_complete()                         │
  └───────────────────────────────────────────┘

  ┌───────────────────────────────────────────┐
  │ Contacts                                  │
  │                                           │
  │ - initialize(contacts_list)               │
  │ - add(diary)                              │
  │ - view_contacts_list()                    │
  └───────────────────────────────────────────┘


```

_Also design the interface of each class in more detail._

```python
class Diary:
    def __init__(self):
        # Parameters:
        #   entries_list: a list of entries
        # Side-effects:
        #   None
        pass # No code here yet

    def add(self, entry):
        # Parameters:
        #   entry: an instance of the #DiaryEntry class
        # Side-effects:
        #   adds an entry to the #entries_list
        # Returns:
        #   None
        pass # No code here yet

    def read_entries(self):
        # Parameters:
        #   None
        # Side-effects:
        #   None
        # Returns:
        #   a list of all diary entries
        pass # No code here yet

    def select_best_entry_to_read(minutes, wpm):
        # Parameters:
        #   minutes: an integer representing how many minutes the user has to read
        #   wpm: an integer representing how many words a user can read per minutes
        # Side-effects:
        #   None
        # Returns:
        #   a diary entry a user can read
        pass # No code here yet


class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: a string representing an entry title
        #   contents: a stirng representing the entry contents
        # Side-effects:
        #   None
        pass # No code here yet


class TodoList:
    def __init__(self):
        # Parameters:
        #   todo_list: a list of tasks
        # Side-effects:
        #   None
        pass # No code here yet

    def add(task):
        # Parameters:
        #   task: an instance of the #Todo class
        # Side-effects:
        #   adds a task to the #todo_list
        # Returns:
        #   None
        pass # No code here yet

    def incomplete_tasks():
        # Parameters:
        #   None
        # Side-effects:
        #   None
        # Returns:
        #   A list of all incomplete tasks
        pass # No code here yet

    def complete_tasks():
        # Parameters:
        #   None
        # Side-effects:
        #   None
        # Returns:
        #   A list of all complete tasks
        pass # No code here yet


class Todo:
    def __init__(self, task):
        # Parameters:
        #   task: a string representing a task
        #   complete: a boolean stating whether a task is complete
        # Side-effects:
        #   None
        pass # No code here yet

    def mark_complete()
        # Parameters:
        #   None
        # Side-effects:
        #   Marks a task's complete state as True
        pass # No code here yet

class Contacts:
    def __init__(self):
        # Parameters:
        #   contacts_list: a list of contacts
        # Side-effects:
        #   None
        pass # No code here yet

    def add_number(diary)
        # Parameters:
        #   entry: an instance of the DiaryEntry class
        # Side-effects:
        #   Adds mobile numbers to the #contacts_list
        # Returns:
        #   None
        pass # No code here yet

    def view_contacts_list()
        # Parameters:
        #   None
        # Side-effects:
        #   None
        # Returns:
        #   a list of all mobile numbers
        pass # No code here yet

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python

"""
Given a diary entry
#read_entries returns a list
containing the diary entry
"""
diary = Diary()
entry = DiaryEntry("Title 1", "Contents 1")
diary.add(entry)
diary.read_entries() # => [entry]

"""
Given 3 diary entries
#read_entries returns a list
containing the 3 diary entries
"""
diary = Diary()
entry_1 = DiaryEntry("Title 1", "Contents 1")
entry_2 = DiaryEntry("Title 2", "Contents 2")
entry_3 = DiaryEntry("Title 3", "Contents 3")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
diary.read_entries() # => [entry_1, entry_2, entry_3]

"""
Given 2 diary entries
and 2 wpm and 2 minutes
#select_best_entry_to_read returns the diary entry instance
closest to the length the user can read
"""
diary = Diary()
entry_1 = DiaryEntry("Title 1", "Contents 1")
entry_2 = DiaryEntry("Title 2", "Hi there contents 2")
diary.add(entry_1)
diary.add(entry_2)
diary.select_best_entry_to_read(2, 2) # => entry_2

"""
Given 3 diary entries, 
2 shorter and 1 longer
and given 3 wpm and 2 minutes
#select_best_entry_to_read returns the diary entry instance
closest to the length the user can read
"""
diary = Diary()
entry_1 = DiaryEntry("Title 1", "Contents 1")
entry_2 = DiaryEntry("Title 2", "Hello and welcome again to contents 2")
entry_3 = DiaryEntry("Title 3", "Hi there contents 3")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
diary.select_best_entry_to_read(3, 2) # => entry_3

"""
Given 3 diary entries, 
all longer than the length the user can read
and given 2 wpm and 3 minutes
#select_best_entry_to_read returns None
"""
diary = Diary()
entry_1 = DiaryEntry("Title 1", "Hi there, have you read about contents 1?")
entry_2 = DiaryEntry("Title 2", "Hello and welcome again to contents 2")
entry_3 = DiaryEntry("Title 3", "Goodbye and see you all tomorrow at contents 3")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
diary.select_best_entry_to_read(2, 3) # => None

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
"""
#Diary class
Initially #read_entries returns an empty list
When no entries have been added yet
"""
diary = Diary()
diary.read_entries() # => []

"""
#Diary class
Initially #select_best_entry_to_read returns None
Given 2 minutes and 2 wpm
But no entries have been added yet
"""
diary = Diary()
diary.select_best_entry_to_read(2, 2) # => None

"""
#DiaryEntry class
When an entry has been created
Returns the entry's title and contents
"""
entry = DiaryEntry("Title 1", "Contents 1")
entry.title # => "Title 1"
entry.contents # => "Contents 1"

```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
