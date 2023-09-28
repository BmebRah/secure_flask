class TODO:
    def __init__(self, mobile):
        self.contacts=[]
        self.mobile=mobile
        self.todos=[]
    def add_task(self, task):
        self.todos.append(task)
        return self.todos
    
