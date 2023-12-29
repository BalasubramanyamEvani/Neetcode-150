class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mem = {}
        for num in nums:
            mem[num] = mem.get(num, 0) + 1
        sortedmem = sorted(mem.items(), key=lambda x: (x[1], -x[0]))
        ret = []
        for k, v in sortedmem:
            ret.extend([k] * v)
        return ret
