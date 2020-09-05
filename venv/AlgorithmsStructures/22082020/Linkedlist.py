class LinkedElement:
    def __init__(self, value, prev=None, next_=None):
        self.value = value
        self.prev = prev
        self.next = next_

    def __str__(self):
        prev_str = "<->" if self.prev else ""
        next_str = str(self.next) if self.next else ""
        return f"{prev_str} {self.value} {next_str}"


class LinkedList:
    def __init__(self):
        self.__first = None

    def _get_last_element(self):
        if self.__first is None:
            return None
        current = self.__first
        while True:
            if current.next is None:
                return current
            current = current.next

    def append(self, value):
        lelement = LinkedElement(value)
        if self._get_last_element() == None:
            self.__first = lelement
            return
        last = self._get_last_element()
        last.next = lelement


        elem = LinkedElement(value)
        if self.__first is None:
            self.__first = elem
            return
        last = self._get_last_element()
        last.next = elem
        elem.prev = last


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

ll2 = LinkedList()
ll.append(4)
ll.append(5)
ll.extend(ll2)

ll.print()
