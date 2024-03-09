class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        l = 0
        r = 0
        currsum = 0
        ret = math.inf
        while r < N:
            currsum += nums[r]
            if currsum >= target:
                while l <= r and currsum >= target:
                    currsum -= nums[l]
                    l += 1
                l -= 1
                winsize = r - l + 1
                ret = min(ret, winsize)
                l += 1
            r += 1
        return ret if ret != math.inf else 0
