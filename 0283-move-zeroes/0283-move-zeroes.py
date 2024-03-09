class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        r = 0
        zeroindex = -1
        while r < N:
            if nums[r] == 0 and zeroindex == -1:
                zeroindex = r
            elif nums[r] != 0 and zeroindex != -1:
                nums[zeroindex], nums[r] = nums[r], nums[zeroindex]
                zeroindex += 1
            r += 1
