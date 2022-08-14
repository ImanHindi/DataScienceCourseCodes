from collections import deque
class deque_class:
    def __init__(self):
        self._deque = []

    def pop(self):
        if len(self._deque) < 1:
            return None
        return self._deque.pop()

    def push(self, item):
        self._deque.append(item)

    def size(self):
        return len(self._deque)
        
x = deque_class()

number=deque()

class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

x = Stack()

number.append(10)
number.append('a')
number.append('1')

id(number[3])
id(number[4])
number.pop()
number.popleft()

l=[]
l.append('a')
l.append(1)
l.append('b')

l.pop(0)