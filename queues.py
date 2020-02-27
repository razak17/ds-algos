""" Queues """

class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty!")
        return self._data[self._front]
    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty!")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer
    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self.data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

cc = ArrayQueue()
# print(cc.__len__())
cc.enqueue(5)
cc.enqueue(1)
cc.enqueue(8)
# print(cc.__len__())
cc.dequeue()
# print(cc.__len__())

""" Double - Ended Queues or Deque """

class ArrayDeque:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    def __len__(self):
        return self._size



""" Much Simpler Implementation of the queue data structure"""

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, e):
        self.items.insert(0, e)

    def dequeue(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        # Last item
        return self.items[-1] if self.items else None
    
    def first(self):
        return self.items[0] if self.items else None
    
    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size == 0

def main():
    cc = Queue()
    for i in range(7):
        cc.enqueue(i)
    print(cc.size())
    print(cc.peek())
    print(cc.first())
    print(cc.is_empty())

if __name__ == "__main__":
    main()


