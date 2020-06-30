class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        self.size = 0

# Create interface/patter to feed in any stack implementation?

class LinkedListStack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        if(self._isEmpty):
            self.head = Node(value)
        else:
            newNode = Node(value)
            self.head.next = newNode
            newNode.previous = self.head
            self.head = newNode
        self.size += 1

    def pop(self):
        if(self._isEmpty()):
            raise IndexError("Stack is empty")
        else:
            popped = self.head.value
            self.head = self.head.previous
            return popped

    def _isEmpty(self):
        return self.head is None

    def _peek(self):
        return self.head.value
