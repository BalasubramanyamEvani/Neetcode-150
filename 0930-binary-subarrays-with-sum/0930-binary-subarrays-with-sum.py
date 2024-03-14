class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        N = len(nums)
        l = 0
        r = 0
        currsum = 0
        count = 0
        mem = {}
        while r < N:
            currsum += nums[r]
            if currsum == goal:
                count += 1
            if currsum - goal in mem:
                count += mem[currsum - goal]
            mem[currsum] = mem.get(currsum, 0) + 1
            r += 1
        return count
        