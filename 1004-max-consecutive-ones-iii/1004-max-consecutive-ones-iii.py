class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        N = len(nums)
        ret = 0
        while r < N:
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            else:
                ret = max(ret, r - l + 1)
            r += 1
        return ret
