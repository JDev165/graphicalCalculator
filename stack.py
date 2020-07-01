# Linked List Stack vs Array/List Stack
# LLS better in this case because push/pop is O(1)
# ALS ammortized worst case is O(n) becuase of the resize (python arrays/list would still have to do this in the background)
# Chose speed over space. LLS use up extra space for pointer references.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

# Create interface/patter to feed in any stack implementation?

class LinkedListStack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, value):
        if(self._isEmpty):
            self.head = Node(value)
            self.tail = self.head
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

    def size(self):
    	return self.size
