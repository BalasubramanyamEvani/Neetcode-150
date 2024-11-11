class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        r = 0
        l = 0
        N = len(nums) - 1
        currsum = 0
        currmax = -math.inf
        while r <= N:
            currsum += nums[r]
            if r - l + 1 == k:
                avg = currsum / k
                currmax = max(currmax, avg)
                currsum -= nums[l]
                l += 1
            r += 1
        return currmax
