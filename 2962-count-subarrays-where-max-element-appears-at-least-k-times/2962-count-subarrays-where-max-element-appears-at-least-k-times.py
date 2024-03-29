class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxnum = max(nums)
        l = 0
        count = 0
        maxnum_count = 0
        for r, num in enumerate(nums):
            if num == maxnum:
                maxnum_count += 1
            while maxnum_count == k and l <= r:
                if nums[l] == num:
                    maxnum_count -= 1
                l += 1
            count += l
        return count