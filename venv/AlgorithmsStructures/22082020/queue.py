"""
1. Write a function which empties a stack element-by-element and prints them.
2. Implement the following as operations on stack, assuming the stack represents browser tab history:
- Visited google.com
- Visited yahoo.com
- Back in history to google.com
- Visited amazon.com
3. Print the stack after the above operations
"""


class Queue:
    def __init__(self):
        self.__stack = []

    def push(self, v):
        self.__stack.append(v)

    def pop(self):
        return self.__stack.pop(0)

    def peek(self):
        return self.__stack[0]

    def __len__(self):
        return len(self.__stack)

    def is_empty(self):
        if not self.__stack:
            return self.__stack == []
        else:
            return False


def print_and_empty_stack(s):
    assert isinstance(s, Queue)
    while not s.is_empty():
        print(s.pop())


if __name__ == "__main__":
    history = Queue()

    history.push("google.com")
    history.push("yahoo.com")
    print(history.is_empty())
    history.pop()
    history.push("amazon.com")
    print_and_empty_stack(history)
