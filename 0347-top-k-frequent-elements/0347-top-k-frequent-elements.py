class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        heap = []
        for key, v in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (v, key))
            elif v > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (v, key))
        return [item[1] for item in heap]
