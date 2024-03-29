class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0
        mem = {}
        maxlen = -math.inf
        for r, ch in enumerate(s):
            mem[ch] = mem.get(ch, 0) + 1
            while len(mem) > k and l <= r:
                mem[s[l]] -= 1
                if mem[s[l]] == 0:
                    del mem[s[l]]
                l += 1
            maxlen = max(maxlen, r - l + 1)
        return maxlen
