class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mem = {}
        counts = {}
        for i, num in enumerate(nums):
            if num not in mem:
                mem[num] = {}
                mem[num]["left"] = i
            mem[num]["right"] = i
            counts[num] = counts.get(num, 0) + 1
        maxnum = max(counts.values())
        ret = math.inf
        for k, v in mem.items():
            if counts[k] == maxnum:
                l, r = v["left"], v["right"]
                ret = min(ret, r - l + 1)
        return ret
