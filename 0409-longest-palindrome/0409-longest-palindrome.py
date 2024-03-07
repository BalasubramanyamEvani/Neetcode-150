class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        ret = 0
        foundodd = False
        for k in counts.keys():
            if counts[k] & 1 != 1:
                ret += counts[k]
            else:
                ret += counts[k] - 1
                foundodd = True
        return ret + (1 if foundodd else 0)
