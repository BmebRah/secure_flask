from lib.todo import *


# It instansates with a string and int parameters

def test_it_initialises_with_string_and_int_parameters():
    instance = TODO("mobile")
    assert instance.contacts == []
    assert instance.mobile == "mobile"

