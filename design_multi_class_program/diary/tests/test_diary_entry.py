from lib.diary_entry import *

# Given an entry in the diary 
# It returns the time it takes to read entriy at a given speed of reading 

def test_it_adds_diary_entries():
    add_reading_time = Diaryentry("title")
    assert add_reading_time.add_entries() == ["title"]


def test_it_returns_reading_time_for_given_entry_per_speed_of_reading():
    time_for_reading = Diaryentry("title")
    assert time_for_reading.chunk_read(6, 3) == 2

    