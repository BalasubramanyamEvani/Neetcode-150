class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        slen = len(s)
        mem = {}
        for i in range(ord("A"), ord("Z") + 1):
            mem[chr(i)] = 0
        res = -1
        l = 0
        for r in range(slen):
            mem[s[r]] += 1
            window_len = r - l + 1
            if window_len - max(mem.values()) <= k:
                res = max(res, window_len)
            else:
                mem[s[l]] -= 1
                l += 1
        return res
