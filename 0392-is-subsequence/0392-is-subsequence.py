class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        if n1 > n2:
            return False
        ptr1 = 0
        for ch in t:
            if  ptr1 < n1 and ch == s[ptr1]:
                ptr1 += 1
        return ptr1 == n1
