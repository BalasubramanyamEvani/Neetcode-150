class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        nr, nc = len(matrix), len(matrix[0])
        for r in range(nr):
            for c in range(nc):
                if len(heap) < k:
                    heapq.heappush(heap, -matrix[r][c])
                elif heap[0] < -matrix[r][c]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, -matrix[r][c])
        return -heap[0]
