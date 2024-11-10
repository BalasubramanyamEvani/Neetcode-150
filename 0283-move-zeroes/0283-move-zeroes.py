class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = -1
        for i, num in enumerate(nums):
            if num == 0 and zero == -1:
                zero = i
            elif num != 0 and zero >= 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
            