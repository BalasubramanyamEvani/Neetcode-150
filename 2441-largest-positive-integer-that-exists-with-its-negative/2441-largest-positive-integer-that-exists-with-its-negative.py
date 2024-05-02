class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ret = -1
        if nums[0] > 0 or nums[-1] < 0:
            return -1
        l, r = 0, len(nums) - 1
        while l < r:
            if abs(nums[l]) == nums[r]:
                ret = nums[r]
                break
            if abs(nums[l]) > nums[r]:
                l += 1
            else:
                r -= 1
        return ret
