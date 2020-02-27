
""" 
List of Elements ordered from most frequently accessed to least


"""
class FavoriteList:

    #--------------------------nested _item class ---------------------------
    class _item:
        __slots__ = '_value', '_count'
        def __init__(self, e):
            self._value = e
            self._count = 0

    #--------------------------nonpublic utilities ---------------------------
    def _find_position(self, e):
        # search for e and return its position
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk
    def _move_up(self, p):
        # move p earlier in list based on access count
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while (walk != self._data.first() and cnt > self.data.before(walk).element()>_count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))
        
    #-----------------------------public methods ------------------------------
    def __init__(self):
        # create empty list of favs
        self._data = PositionList()
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data) == 0
    def access(self, e):
        # access e thereby increasing its access count
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(self._item(e))
        p.element()._count += 1
        self._move_up(p)
    def remove(self, e):
        # remove e fromlist of favs
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)
    def top(self, k):
        # generate sequence of top k elements based on access count
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)

"""
    List of elements ordered with move-to-front heuristic
"""

class FavoritesListMTF(FavoriteList):

    # override _move_up to provide move-to-front semantics
    def _move_up(self, p):
        # move accesses item at position p to front of list
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))
    # Top is overriden cos list is no longer sorted
    def top(self, k):
        # sequence of top k elements based on access count
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k!")

        # make copy of original list
        temp = PositionList()
        for item in self._data:
            temp.add_last(item)

        for j in range(k):
            highPos = temp.first()
            walk = temp.after(highPos)
        while walk is not None:
            if walk.element()._count > highPos._element()._count:
                highPos = walk
            walk = temp.after(walk)
        yield highPos.element()._value
        temp.delete(highPos)