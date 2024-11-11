class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        ops = 0
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == k:
                ops += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
        return ops
