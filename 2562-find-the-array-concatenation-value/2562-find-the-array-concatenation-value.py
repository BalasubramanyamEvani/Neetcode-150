class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        N = len(nums)
        l, r = 0, N - 1
        concat_value = 0
        while l < r:
            digits = int(math.log10(nums[r])) + 1
            concat_value += (nums[l] * 10**digits) + nums[r]
            l += 1
            r -= 1
        if N & 1:
            concat_value += nums[l]
        return concat_value
