import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k):
            return sum([math.ceil(p / k) for p in piles]) <= h
            
        l = math.ceil(sum(piles)/h)
        r = max(piles)
        curr = -1
        while l <= r:
            mid = l + (r - l) // 2
            if possible(mid):
                curr = mid
                r = mid - 1
            else:
                l = mid + 1
        return curr
