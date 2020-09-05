# Implementation of a custom iterator
class MyRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):  # called when iterator is created
        self.i = self.start - self.step
        return self

    def __next__(self):  # called on next
        self.i += self.step
        if self.i <= self.stop:
            return self.i
        else:
            raise StopIteration


for i in MyRange(10, 100, 10):
    print(i)
