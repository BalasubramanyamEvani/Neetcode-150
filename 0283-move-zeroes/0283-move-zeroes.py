class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        lastzero_index = -1
        i = 0
        numslen = len(nums)
        while i < numslen:
            if nums[i] == 0 and lastzero_index == -1:
                lastzero_index = i
            if nums[i] != 0 and lastzero_index >= 0:
                swap(i, lastzero_index)
                lastzero_index += 1
            i += 1
