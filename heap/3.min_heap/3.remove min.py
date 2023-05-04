#  here we build a heap.
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def build_heap(self, arr):
        self.heap = arr
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.min_heapify(i)

    def min_heapify(self, i):
        n = len(self.heap)
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.swap(i, smallest)
            self.min_heapify(smallest)

    def remove_min(self):
        n = len(self.heap)
        if n == 0:
            return None
        self.swap(0, n - 1)
        min_val = self.heap.pop()
        self.min_heapify(0)
        return min_val


arr = [4, 12, 7, 3, 9, 8, 5, 6]
my_min_heap = MinHeap()
my_min_heap.build_heap(arr)
print(my_min_heap.heap)

my_min_heap.remove_min()
print('\n after deletion : ', my_min_heap.heap)
