"""
Node - Allocated to each element. maintains a reference to is neighboring nodes

head - first node
tail - last node(has None as its next reference)

"""

""" Singly Linked List 
tail of list links to None

Each node keeps a refernce to the node after it


"""

class LinkedStack:
    """FIFO Stack implementation using a singly linked list"""
    class _Node:
        #Streamline memory usage
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        self._head = None
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def push(self, e):
        """ Add element to the top of the stack """
        self._head = self._Node(e, self._head)
        self._size += 1
    def top(self):
        """ Return element at the top of the stack """
        if self.is_empty():
            raise Empty("Stack is empty!")
        return self._head._element
    def pop(self):
        """ Remove and return element from top of the stack """
        if self.is_empty():
            raise Empty("Stack is empty!")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

cc = LinkedStack()
cc.push(2)
print(cc.top())