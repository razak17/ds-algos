from hashTables import SortedTableMap

class CostPerformanceDatabase:
    # A database with maximal (cost, performance) pairs

    def __init__(self):
        self._M = SortedTableMap()
    
    def __len__(self):
        return len(self._M)

    def best(self, c):
        # return (c, p) pairs with largest cost not exceeding c.
        return self._M.find_le(c)

    def add(self, c, p):
        other = self._M.find_le(c)
        if other is not None and other[1] >= p:
            return
        self._M[c] = p
        # remove any pairs that are dominated by (c, p)
        other = self._M.find_gt(c)
        while other is not None and other[1] <= p:
            del self._M[other[0]]
            other = self._M.find_gt(c)

cc = CostPerformanceDatabase()
cc.add(200000, 200)
cc.add(150000, 120)
cc.add(120000, 100)
cc.add(100000, 90)
cc.add(75000, 80)
print(cc.best(95000))
print(cc.__len__())
