from linkedLists import _DoublyLinkedBase

""" The Positional List ADT
Used to access nodes by their positon

"""

# Positional Class List based on a doubly linked list

class PositionalList(_DoublyLinkedBase):
    class Position:
        # An abstraction representing the location of a single ele
        
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            # return true if other is a Position repping the same location as self
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            # return true if other does not rep same location (opposite of __eq__)
            return not(self == other)
        
    #---------- utility method ----------
    def _validate(self, p):
        # return position's node
        if not isinstance(p, self.Position):
            raise TypeError("p must be a proper position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid!")
        return p._node

    def _make_position(self, node):
        # return position instance for given node
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)
    
    #---------- accessors ---------
    def first(self):
        # return first position in list
        return self._make_position(self._header._next)

    def last(self):
        # return last position inlist
        return self._make_position(self._trailer._prev)

    def before(self, p):
        # return position just before position p
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self.validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        # forward iteration of list elements
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
            
    #----------mutators -----------
    # override inherited version to return Position rather than noode
    def _insert_between(self, e, pre, succ):
        # add element between eexisting nodes and return new positon
        node = super()._insert_between(e, pre, succ)
        return self._make_position(node)

    def add_first(self, e):
        # insert e at front of list and return new position
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        # insert e before position p and return new position
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        # delete and return element at position p
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        # replace element at position p with e
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

# cc = PositionalList()
# print(cc.add_last(8))
# print(cc.before(cc.add_last(2)))
# print(cc.last())


def insertion_sort(L):
    L = PositionalList()
    if len(L) > 1:
        marker = L.first()
        while marker != l.last():
            pivot = l.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)
    return L

print(insertion_sort([2,4,6,3,2,1]))