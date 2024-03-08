class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxfreq = 0
        mem = {}
        for num in nums:
            mem[num] = mem.get(num, 0) + 1
            if mem[num] > maxfreq:
                maxfreq = mem[num]
        ret = 0
        for v in mem.values():
            if v == maxfreq:
                ret += v
        return ret
        