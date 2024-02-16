import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
        res = []
        for num in counts.keys():
            heapq.heappush(res, (counts[num], num))
        while k > 0 and res:
            count, num = heapq.heappop(res)
            to_remove = min(count, k)
            k -= to_remove
            count -= to_remove
            if count > 0:
                heapq.heappush(res, (count, num))
        return len(res)
