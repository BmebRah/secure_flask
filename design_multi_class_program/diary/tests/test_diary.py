from lib.diary import *

# It instantiates succefully 
def test_it_instantiate_with_a_string_and_dictionary():
    instance = Diary("entry1", "plan a gataway trip", "todo", "shopping")
    assert instance.title == "entry1"
    assert instance.contents == "plan a gataway trip"

# Given a task with title an contents
# it adds task to a dictionary as {title: contents}

def test_it_adds_diary_entries():
    add_entry = Diary("entry1", "contents", "todo", "shopping")
    assert add_entry.add_entries() == {"entry1" : "contents", 'todo': 'shopping'}

# A user can read past entries

def test_it_returns_entry_contents():
    read_entries = Diary("entry1", "contents", "todo", "shopping")
    assert read_entries.read_entries() ==  {'entry1': 'contents'}