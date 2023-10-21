class MedianFinder:
    def __init__(self):
        self.low_max_heap = []
        self.high_min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low_max_heap, -num)
        if self.high_min_heap:
            high_min = heapq.heappop(self.high_min_heap)
            heapq.heappush(self.low_max_heap, -high_min)
        
        while len(self.low_max_heap) - len(self.high_min_heap) > 1:
            low_max = heapq.heappop(self.low_max_heap)
            heapq.heappush(self.high_min_heap, -low_max)
        
    def findMedian(self) -> float:
        assert len(self.low_max_heap) - len(self.high_min_heap) <= 1
        
        low_max = -self.low_max_heap[0]
        
        # only one element
        if not self.high_min_heap:
            return low_max
        
        # odd elements
        if len(self.low_max_heap) - len(self.high_min_heap) == 1:
            return low_max
        
        high_min = self.high_min_heap[0]
        
        # even elements
        return (low_max + high_min) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()