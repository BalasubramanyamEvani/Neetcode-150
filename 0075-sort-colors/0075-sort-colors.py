class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        low = 0
        mid = 0
        high = N - 1
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        while mid <= high:
            if nums[mid] == 0:
                swap(mid, low)
                mid += 1
                low += 1
            elif nums[mid] == 2:
                swap(mid, high)
                high -= 1
            else:
                mid += 1
