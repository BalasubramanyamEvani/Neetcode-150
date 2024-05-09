class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = [-num for num in happiness]
        heapq.heapify(heap)
        count, ptr = 0, 0
        while k:
            incr = -heapq.heappop(heap)
            if incr - ptr > 0:
                incr -= ptr
            else:
                break
            count += incr
            k -= 1
            ptr += 1
        return count
