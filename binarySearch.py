import os

# def binary_search(aList, num):
#     aList.sort()
#     while aList:
#         mid = len(aList) // 2
#         if aList[mid] == num:
#             return True
#         elif aList[mid] > num:
#             aList = aList[:mid]
#         elif aList[mid] < num:
#             aList = aList[num + 1:]
#     return False

# print(binary_search([2,3,4,5,6,7,8,9,1,0], 22))

def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

# print(binary_search([2,3,4,5,6,7,8,9,1], 5, 0, 8))

def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            child_path = os.path.join(path, filename)
            total += disk_usage(child_path)

    print("{0:<7}".format(total), path)
    return total


''' Storing high scores for a game .'''

class GameEntry:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name
    def get_score(self):
        return self._score
    
    def __str__(self):
        return("({0}, {1})".format(self._name, self._score))

class ScoreBoard:
    def __init__(self, capacity=10):
        self._board = [None] * capacity
        self._n = 0
    
    def __getitem__(self, k):
        return self._board[k]
    def __str__(self):
        return '\n'.join(str(self._board[j])for j in range(self._n))
    def add(self, entry):
        score = entry.get_score()
        good = self._n < len(self._board) or score > self._board[-1].get_score()
        if good:
            if self._n < len(self._board):
                self._n += 1

            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]
                j -= 1
            self._board[j] = entry

c = GameEntry("Anz", 100)
print(c.get_name())
print(c.get_score())
# print(c.__str__())

d = GameEntry("Rich", 120)
e = GameEntry("Zap", 80)
f = GameEntry("Sue", 90)
g = GameEntry("Stewe", 20)
h = GameEntry("Brad", 55)
i = GameEntry("Axl", 85)
j = GameEntry("Brick", 70)
k = GameEntry("Heck", 50)
l = GameEntry("Ian", 45)
m = GameEntry("Ricky", 150)

cc = ScoreBoard()
cc.add(c)
cc.add(d)
cc.add(e)
cc.add(f)
cc.add(g)
cc.add(h)
cc.add(i)
cc.add(j)
cc.add(k)
cc.add(l)
cc.add(m)
print(cc.__str__())

import heapq



