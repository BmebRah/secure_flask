import math

class Diaryentry():
    def __init__(self, entry):
        self.reading_time = []
        self.entry=entry

    def add_entries(self):
        self.reading_time.append(self.entry)
        return self.reading_time

# As a user
# So that I can reflect on my experiences in my busy day
# I want to select diary entries to read based on how much time I have and my reading speed
    def chunk_read(self, time, wpm):
        words = self.add_entries()[0].split(" ")
        words_reader_can_read = words * wpm
        chunk_per_minute = math.ceil(time / len(words_reader_can_read))
        print(chunk_per_minute)
        return chunk_per_minute
        
        