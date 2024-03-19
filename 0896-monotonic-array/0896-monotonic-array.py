class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        N = len(nums)
        if N <= 2:
            return True
        increasing = False
        decreasing = False
        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                increasing = True
            elif nums[i] < nums[i - 1]:
                decreasing = True
        if increasing and decreasing:
            return False
        return True
