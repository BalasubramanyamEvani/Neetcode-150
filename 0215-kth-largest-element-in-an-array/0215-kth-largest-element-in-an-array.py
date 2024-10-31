import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # O(n + klogk)
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        return heap[0] if heap else -1
