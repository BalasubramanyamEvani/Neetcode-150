class SmallestInfiniteSet:

    def __init__(self, min_pos=1, max_pos=1000):
        self._nums = set([num for num in range(min_pos, max_pos + 1)])
        self._minheap = [num for num in range(min_pos, max_pos + 1)]
        heapq.heapify(self._minheap)
        
    def popSmallest(self) -> int:
        # if no elements return -1
        if not len(self._minheap):
            return -1
        # pop the smallest from min heap
        smallest = heapq.heappop(self._minheap)
        # remove the smallest from the set
        self._nums.remove(smallest)
        # sanity check
        assert len(self._minheap) == len(self._nums)
        # return smallest
        return smallest
        
    def addBack(self, num: int) -> None:
        # if num in nums set then simply return 
        if num in self._nums:
            return
        # else push it to min heap
        heapq.heappush(self._minheap, num)
        # and add it to the set as well
        self._nums.add(num)
        # sanity check
        assert len(self._minheap) == len(self._nums)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)