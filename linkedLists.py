""" Doubly Linked Lists
# Each node in list keeps a reference to the node before it and a reference to the node after it.

# Allows for insertion and deletion at arbitrary positions within list

Dummy Nodes(sentinels)
 - Header - at the beginning of the list
 - Trailer - at the end of the list

 """


class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation.”"""
    class _Node:
        __slot__ = '_elements', '_prev', '_next'
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def _insert_between(self, e, pre, succ):
        # Add element between two existing nodes
        newest = self._Node(e, pre, succ)
        pre._next = newest
        succ._prev = newest
        self._size += 1
        return newest
    def _delete_node(self, node):
        # delete nonsentinel node from list and return its elements
        pre = node._prev
        succ = mode._next
        pre._next = sucessor
        succ._pre = pre
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

cc = _DoublyLinkedBase()

# print(cc.is_empty())