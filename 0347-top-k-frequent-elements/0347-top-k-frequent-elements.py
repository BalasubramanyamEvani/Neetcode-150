class Entry:
    def __init__(self, k, v):
        self.k = k
        self.v = v
    
    def __str__(self):
        return f"{self.k}: {self.v}"
        
        
class Heap:
    def __init__(self, n):
        self.n = n
        self.heap = []
        self.ptr = -1
    
    def __len__(self):
        return self.ptr + 1
    
    def rightChild(self, i):
        c = 2 * i + 2
        return c if c <= self.ptr else None
    
    def leftChild(self, i):
        c = 2 * i + 1
        return c if c <= self.ptr else None
    
    def parent(self, i):
        return (i - 1) // 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, entry):
        assert self.ptr != self.n - 1
        self.heap.append(entry)
        self.ptr += 1
        self.heapifyUp(self.ptr)
    
    def remove(self):
        assert self.ptr >= 0
        curr_most_frequent = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.ptr -= 1
        self.heapifyDown(0)
        return curr_most_frequent
        
    def heapifyUp(self, i):
        curr_index = i
        parent_index = self.parent(curr_index)
        while parent_index != -1 and self.heap[parent_index].v < self.heap[curr_index].v:
            self.swap(parent_index, curr_index)
            curr_index = parent_index
            parent_index = self.parent(curr_index)
    
    def heapifyDown(self, i):
        curr_index = i
        while True:
            left_index = self.leftChild(curr_index)
            right_index = self.rightChild(curr_index)
            
            max_index = curr_index
            
            if left_index and self.heap[left_index].v > self.heap[max_index].v:
                max_index = left_index
            if right_index and self.heap[right_index].v > self.heap[max_index].v:
                max_index = right_index
            
            if max_index == curr_index:
                break
            
            self.swap(max_index, curr_index)
            curr_index = max_index
    
    def __str__(self):
        res = []
        for num in self.heap:
            res.append(str(num))
        return " ".join(res)

    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mem = {}
        for num in nums:
            if num in mem:
                mem[num] += 1
            else:
                mem[num] = 1
        maxheap = Heap(len(mem))
        for key, val in mem.items():
            maxheap.insert(Entry(key, val))
        res = []
        for i in range(k):
            entry = maxheap.remove()
            res.append(entry.k)
        return res
            