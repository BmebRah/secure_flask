from lib.diary import * 
from lib.todo import *

# Given a task
# It adds task to diary

def test_it_adds_task_to_diary():
    instance = TODO("mobile")
    task1 = Diary("title", "contents", "task", "task_content").add_entries()
    result = instance.add_task("mobile")
    assert result == ["mobile"]
    