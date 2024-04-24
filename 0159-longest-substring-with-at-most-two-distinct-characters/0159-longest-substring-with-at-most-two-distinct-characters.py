class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        N = len(s)
        l, r = 0, 0
        mem = {}
        ret = 0
        while r < N:
            mem[s[r]] = mem.get(s[r], 0) + 1
            while len(mem) > 2:
                mem[s[l]] -= 1
                if mem[s[l]] == 0:
                    del mem[s[l]]
                l += 1
            ret = max(ret, r - l + 1)
            r += 1
        return ret
