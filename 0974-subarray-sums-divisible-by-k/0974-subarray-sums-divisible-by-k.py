class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        currsum = 0
        ret = 0
        mem = {}
        for num in nums:
            currsum = (currsum + num) % k
            if currsum == 0:
                ret += 1
            if currsum - k in mem:
                ret += mem[currsum - k]
            mem[currsum - k] = mem.get(currsum - k, 0) + 1
        return ret
