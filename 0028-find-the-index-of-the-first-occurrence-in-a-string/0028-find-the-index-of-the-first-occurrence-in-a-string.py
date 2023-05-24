class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def found(s, e):
            i = 0
            while s < e:
                if haystack[s] != needle[i]:
                    return False
                s += 1
                i += 1
            return True
            
        haystack_len = len(haystack)
        window = len(needle)
        i = 0
        while i <= haystack_len - window:
            start = i
            end = i + window
            if found(start, end):
                return i
            i += 1
        return -1
                