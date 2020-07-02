# Linked List Stack vs Array/List Stack
# LLS is better in this case because push/pop is O(1)
# ALS ammortized worst case is O(n) because of the resize (python arrays/list would still have to do this in the background)
# Chose speed over space. LLS use up extra space for pointer references.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

# Create interface/patter to feed in any stack implementation?


class LinkedListStack:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def push(self, value):
        if(self._isEmpty()):
            self._head = Node(value)
            self._tail = self._head
        else:
            newNode = Node(value)
            self._head.next = newNode
            newNode.previous = self._head
            self._head = newNode
        self._size += 1

    def pop(self):
        if(self._isEmpty()):
            raise IndexError("Stack is empty")
        else:
            popped = self._head.value
            self._head = self._head.previous
            return popped

    def _isEmpty(self):
        return self._head is None

    def _peek(self):
        return self._head.value

    def size(self):
        return self._size

    def getHead(self):
        return self._head

    def getTail(self):
        return self._tail
