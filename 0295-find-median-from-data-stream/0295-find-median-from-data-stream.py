class MedianFinder:
    def __init__(self):
        self.low_max_heap = []
        self.high_min_heap = []

    def addNum(self, num: int) -> None:
        # insert to low min heap
        heapq.heappush(self.low_max_heap, -num)
        
        # if the maximum in min heap is not <= minimum in high max heap
        # then pop from low and push to high
        if self.high_min_heap and -self.low_max_heap[0] > self.high_min_heap[0]:
            low_max = heapq.heappop(self.low_max_heap)
            heapq.heappush(self.high_min_heap, -low_max)
        # if size difference > 1 then we need to rebalance it
        lN, hN = len(self.low_max_heap), len(self.high_min_heap)
        if lN - hN > 1:
            low_max = heapq.heappop(self.low_max_heap)
            heapq.heappush(self.high_min_heap, -low_max)
        elif hN - lN > 1:
            high_min = heapq.heappop(self.high_min_heap)
            heapq.heappush(self.low_max_heap, -high_min)

    def findMedian(self) -> float:
        lN, hN = len(self.low_max_heap), len(self.high_min_heap)
        # only one element
        if hN == 0:
            return -self.low_max_heap[0]
        
        # odd elements
        if hN != lN:
            if lN > hN:
                return -self.low_max_heap[0]
            else:
                return self.high_min_heap[0]

        # even elements
        low_max = -self.low_max_heap[0]
        high_min = self.high_min_heap[0]
        return (low_max + high_min) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()