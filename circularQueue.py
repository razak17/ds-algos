""" Circular Linked Lists 
tail of list links to the head of the list

"""
class CircularQueue:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        #just return element at the front of the queue
        if self.is_empty():
            raise Empty("Queue is empty!")
        head = self._tail._next
        return head._element
    def dequeue(self):
        #remove and return the first element in the queue
        if self.is_empty():
            raise Empty("Queue is empty!")
        old_head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = old_head._next
        self._size -= 1
        return old_head._element
    def enqueue(self, e):
        #Add element to the back of the queue
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
        self._tail = newest
        self._size += 1
    def rotate(self):
        # rotate front element to the back of the queue
        if self._size > 0:
            self._tail = self._tail._next

cc = CircularQueue()
cc.enqueue(6)
cc.enqueue(8)
print(cc.first())
print(cc.is_empty())