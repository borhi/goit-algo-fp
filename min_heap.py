class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")
        self._swap(0, len(self.heap) - 1)
        item = self.heap.pop()
        if self.heap:
            self._sift_down(0)
        return item

    def is_empty(self):
        return not self.heap

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return 2 * index + 1

    def _right(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_up(self, index):
        while index > 0:
            parent = self._parent(index)
            if self.heap[index] < self.heap[parent]:
                self._swap(index, parent)
                index = parent
            else:
                break

    def _sift_down(self, index):
        size = len(self.heap)
        while True:
            smallest = index
            left = self._left(index)
            right = self._right(index)

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == index:
                break
            self._swap(index, smallest)
            index = smallest
