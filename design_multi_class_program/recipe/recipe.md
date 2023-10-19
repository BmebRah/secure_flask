1. Describe the Problem
Typically you will be given a short statement that does this called a user story. In industry, you may also need to ask further questions to clarify aspects of the problem.

As a user
So that I can record my experiences
I want to keep a regular diary

2. Design the Class System
Design the interfaces of each of your classes and how they will work together to achieve the job of the program. You can use diagrams to visualise the relationships between classes.

Consider pulling out the key verbs and nouns in the problem description to help you figure out which classes and methods to have.

class Diary():
   def __init__(self):
    parameter: 
        - title(string): contents(string) as an input for diary entries
        - a dictionary to save diary entries
    returns: none
    def add_entries(self):
    parameter:
        - none 
    returns:
        nothing
    def read_entries(self):
    parameters:
        - none
    returns:
        - dictionary of entries {title: contents} given as key and value pairs 

class Entries_per_minute():
    def entries_per_time(self, wpm):
    parameters:
        - read_entries()
        - words per minute
    returns:
        - time that can be read for a given reading speed
class TODO():
    parameters:
        - task as string
        - contact as string
    returns:
        - list of tasks and contacts 
┌────────────────────────────┐
│ MusicPlayer                │
│                            │
│ - tracks                   │
│ - add(track)               │
│ - search_by_title(keyword) │
│   => [tracks...]           │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Track(title, artist)    │
│                         │
│ - title                 │
│ - artist                │
│ - format()              │
│   => "TITLE by ARTIST"  │
└─────────────────────────┘
Steps 3, 4, and 5 then operate as a cycle.

# It instantiates succefully 

def test_it_instantiate_with_a_string_and_dictionary():

# Given a task with title an contents
# it adds task to a dictionary as {title: contents}

def test_it_adds_diary_entries():

# Given a title and not entries
# It throws an error

def test_it_throws_an_error_given_a_title_and_not_content():

# Given an entry in the diary 
# It returns the time it takes to read entriy at a given speed of reading 

def test_it_returns_reading_time_for_given_entry_per_speed_of_reading():

# Given a task and contact
# It returns a list of contacts and tasks


<!-- As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary
As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries -->
class TODO():
    parameters:
        - task as string (contact)
        - contact as int (mobile number )
    returns:
        - list of tasks 
        - list of contacts 

# It instansates with a string and int parameters

def test_it_initialises_with_string_and_int_parameters():


# Given a task
# It adds task to diary

def test_it_adds_task_along_side_diary_entries():


# Given a string of contacts and mobile phone number 
# It returns a list of all the mobile phone numbers in all diary entries 

def test_it_adds_contacts_mobile_number_and_return_a_list():
