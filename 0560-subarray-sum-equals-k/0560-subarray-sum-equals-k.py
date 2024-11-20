class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currsum = 0
        N = len(nums)
        ret = 0
        mem = {}
        for num in nums:
            currsum += num
            if currsum == k:
                ret += 1
            if currsum - k in mem:
                ret += mem[currsum - k]
            mem[currsum] = mem.get(currsum, 0) + 1
        return ret
