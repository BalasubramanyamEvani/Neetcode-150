class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mem = {}
        max_count = -1
        curr_count = 0
        i = 0
        slen = len(s)
        while i < slen:
            ch = s[i]
            if ch not in mem:
                curr_count += 1
                mem[ch] = i
                i += 1
            else:
                max_count = max(max_count, curr_count)
                curr_count = 0
                i = mem[ch] + 1
                mem.clear()
       
        if len(mem) > 0:
            max_count = max(max_count, len(mem))
        return max_count if max_count > 0 else 0
