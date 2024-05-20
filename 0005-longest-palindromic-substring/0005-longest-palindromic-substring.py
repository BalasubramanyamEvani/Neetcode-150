class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret, retl, retr = 0, 0, 0
        N = len(s)
        for i in range(N):
            l, r = i, i
            while l >= 0 and r < N and s[l] == s[r]:
                if r - l + 1 > ret:
                    retl = l
                    retr = r
                    ret = r - l + 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < N and s[l] == s[r]:
                if r - l + 1 > ret:
                    retl = l
                    retr = r
                    ret = r - l + 1
                l -= 1
                r += 1
        return s[retl:retr + 1]
