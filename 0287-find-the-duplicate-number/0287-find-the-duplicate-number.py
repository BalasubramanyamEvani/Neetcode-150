class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def count_nums_less_than_equal(n):
            res = 0
            for num in nums:
                if num <= n:
                    res += 1
            return res
        
        N = len(nums) - 1
        low = 1
        high = N
        dup = -1
        while low <= high:
            mid = low + (high - low) // 2
            if count_nums_less_than_equal(mid) > mid:
                dup = mid
                high = mid - 1
            else:
                low = mid + 1
        return dup
