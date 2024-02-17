import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        N = len(heights)
        for i in range(1, N):
            diff = heights[i] - heights[i - 1]
            if diff > 0:
                heapq.heappush(heap, -diff)
                bricks -= diff
                if bricks < 0:
                    if ladders == 0:
                        return i - 1
                    bricks += -heapq.heappop(heap)
                    ladders -= 1
        return N - 1
