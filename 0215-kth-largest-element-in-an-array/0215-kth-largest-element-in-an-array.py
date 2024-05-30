class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def leftChild(self, i):
        return 2 * i + 1
    
    def rightChild(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def heappush(self, num):
        self.heap.append(num)
        curr_index = len(self.heap) - 1
        self.heapifyUp(curr_index)
    
    def heappop(self):
        if not self.heap:
            return - 1

        ret = self.heap[0]
        self.swap(-1, 0)
        self.heap.pop(-1)
        if self.heap:  
            self.heapifyDown(0)
        return ret
    
    def heapifyUp(self, i):
        parent_index = self.parent(i)
        while parent_index >= 0 and self.heap[parent_index] < self.heap[i]:
            self.swap(parent_index, i)
            i = parent_index
            parent_index = self.parent(i)
           
    
    def heapifyDown(self, i):
        left_index = self.leftChild(i)
        right_index = self.rightChild(i)
        curr_max_index = i
        
        if left_index < len(self.heap) and self.heap[left_index] > self.heap[curr_max_index]:
            curr_max_index = left_index
        
        if right_index < len(self.heap) and self.heap[right_index] > self.heap[curr_max_index]:
            curr_max_index = right_index
        
        if curr_max_index != i:
            self.swap(curr_max_index, i)
            self.heapifyDown(curr_max_index)

    def __len__(self):
        return len(self.heap)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = MaxHeap()
        for num in nums:
            max_heap.heappush(num)
            
        for i in range(k - 1):
            max_heap.heappop()
        
        return max_heap.heappop()
