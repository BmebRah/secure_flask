class Diary():
    def __init__(self, title, contents, task, task_content):
        self.title=title
        self.contents=contents
        self.entries = {}
        self.task=task
        self.task_content=task_content
    def add_entries(self):
        self.entries[self.title] = self.contents
        self.entries[self.task] = self.task_content
        return self.entries 
        
    def read_entries(self):
        self.entries[self.contents] = [self.title for self.title in self.add_entries() if self.add_entries()[self.title]]
        # self.entries[self.task] = [self.task for self.task in self.add_entries() if self.add_entries()[self.task]]
        # print(self.entries[self.task])#
        self.entries[self.title]
        return self.entries[self.title]
        


