class Solution:
    def minimumLength(self, s: str) -> int:
        N = len(s)
        if N == 0:
            return 0
        l = 0
        r = N - 1
        while l < r and s[l] == s[r]:
            ch = s[l]
            while l <= r and s[l] == ch:
                l += 1
            while l < r and s[r] == ch:
                r -= 1
        return r - l + 1
