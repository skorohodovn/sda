class Stack:
    def __init__(self):
        self.list = []

    def push(self, value):
        self.list.append(value)
    def pop(self):
        return self.list.pop()
    def __len__(self):
        return(len(self.list))
    def is_empty(self):
        return len(self.list) == 0


s = Stack()
print(f"The stack is empty - {s.is_empty()}")
s.push("first")
s.push("second")
print(f"Stack size - {len(s)}")
print(s.pop())
print(s.pop())