class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        def distance(p2):
            return math.sqrt(p2[0]**2 + p2[1]**2)
        
        for point in points:
            p_distance = distance(point)
            if len(heap) < k:
                heapq.heappush(heap, (-p_distance, point))
            elif -heap[0][0] > p_distance:
                heapq.heappop(heap)
                heapq.heappush(heap, (-p_distance, point))
        ret = []
        while heap:
            ret.append(heapq.heappop(heap)[1])
        return ret
