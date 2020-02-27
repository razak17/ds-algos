from linkedLists import _DoublyLinkedBase


""" Doubly Linked List Implementation of a Deque(Double ended queue)


"""

class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty!")
        return self._header._next._element
    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty!")
        return self._trailer._prev._element
    def insert_first(self, e):
        # insert element to front of the deque
        self._insert_between(e, self._header, self._header._next)
    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)
    def delete_first(self):
        # remove and return element form the front of the deque
        if self.is_empty():
            raise Empty("Deque is empty!")
        return self._delete_node(self._header._next)
    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty!")
        return self._delete_node(self._trailer._prev)

cc = LinkedDeque()
cc.insert_first(3)
cc.insert_last(5)
print(cc.first())