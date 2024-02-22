class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        i = 0
        mem = {}
        ret = 0
        maxlen = 0
        while i < N:
            if s[i] not in mem:
                maxlen += 1
                mem[s[i]] = i
            else:
                i = mem[s[i]]
                ret = max(ret, maxlen)
                mem = {}
                maxlen = 0
            i += 1
        ret = max(ret, maxlen)
        return ret
