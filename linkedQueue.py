class LinkedQueue:
    """ FIFO queue implementation using a singly linked list for storage"""
    
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty!")
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise NameError("Queue is empty!")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
        
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def reverse(self):
        prev = None
        curr = self._head
        while curr != None:
            next_temp = curr._next
            curr._next = prev
            prev = curr
            curr = next_temp
        return prev


cc = LinkedQueue()
cc.enqueue(6)
cc.enqueue(2)
cc.enqueue(2)
cc.enqueue(2)
print(cc.first())