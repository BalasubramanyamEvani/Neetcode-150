class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        mem = {}
        count = 0
        ret = 0
        i = 0
        while i < N:
            ch = s[i]
            if ch not in mem:
                mem[ch] = i
                count += 1
            else:
                ret = max(ret, count)
                i = mem[ch]
                mem = {}
                count = 0
            i += 1
        ret = max(ret, count)
        return ret
