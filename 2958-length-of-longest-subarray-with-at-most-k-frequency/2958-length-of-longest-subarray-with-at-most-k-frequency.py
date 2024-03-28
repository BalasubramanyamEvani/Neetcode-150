class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        mem = {}
        maxlen = -math.inf
        l = 0
        for r, num in enumerate(nums):
            mem[num] = mem.get(num, 0) + 1
            while mem[num] > k:
                mem[nums[l]] -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)
        return maxlen
