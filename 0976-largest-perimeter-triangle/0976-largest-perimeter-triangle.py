class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, key=lambda x: -x)
        N = len(nums)
        for i in range(N - 2): # N - 3 + 1
            num1, num2, num3 = nums[i], nums[i + 1], nums[i + 2]
            if num2 + num3 > num1:
                return num1 + num2 + num3
        return 0
