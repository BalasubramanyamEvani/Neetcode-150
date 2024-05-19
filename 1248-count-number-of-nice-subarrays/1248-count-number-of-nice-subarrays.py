class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l = 0
        r = 0
        mem = {}
        count = 0
        ret = 0
        while r < N:
            if nums[r] % 2 != 0:
                count += 1
            if count == k:
                ret += 1
            if count - k in mem:
                ret += mem[count - k]
            mem[count] = mem.get(count, 0) + 1
            r += 1
        return ret
