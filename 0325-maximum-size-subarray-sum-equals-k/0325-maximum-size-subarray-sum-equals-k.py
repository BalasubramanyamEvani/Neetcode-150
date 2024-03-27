class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        mem = {}
        currsum = 0
        maxlen = 0
        for i, num in enumerate(nums):
            currsum += num
            if currsum == k:
                maxlen = max(maxlen, i + 1)
            if currsum - k in mem:
                maxlen = max(maxlen, i - mem[currsum - k])
            if currsum not in mem:
                mem[currsum] = i
        return maxlen
