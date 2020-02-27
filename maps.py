from _collections_abc import MutableMapping

class MapBase(MutableMapping):

    class _item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key


class UnsortedTableMap(MapBase):
    # Map implementation using unordered list

    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: {}'.format(repr(k)))

    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        self._table.append(self._item(k, v))

    def __delitem__(self, k):
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError('Key Error: {}'.format(repr(k)))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key

class MultiMap:
    # A multimap class built upon use of an underlying map for storage

    _MapType = dict

    def __init__(self):
        self._map = self._MapType()
        self._n = 0

    def __iter__(self):
        # iterate through all (k, v) pairs in mulitmaps
        for k,secondary in self._map.items():
            for v in secondary:
                yield (k, v)

    def add(self, k, v):
        # add pair (k, v) to multimap
        container = self._map.setdefault(k, [])
        container.append(v)
        self._n += 1

    def pop(self, k):
        # remove and return arbitrary (k, v) with key k
        secondary = self._map[k]
        if len(secondary) == 0:
            del self._map[k]
        self._n -= 1
        return (k, v)

    def find(self, k):
        # return arbitrary (k, v) pair with given key
        secondary = self._map[k]
        return (k, secondary[0])

    def find_all(self, k):
        # generate iteration of all (k, v) pairs with given key
        secondary = self._map.get(k, [])
        for v in secondary:
            yield (k, v)
            