class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        org = {}
        for c in s:
            if c in org:
                org[c] += 1
            else:
                org[c] = 1
        for c in t:
            if c in org and org[c] > 0:
                org[c] -= 1
            else:
                return c
        return None
