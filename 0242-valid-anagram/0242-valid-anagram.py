class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = {}
        for c in s:
            if c in smap:
                smap[c] += 1
            else:
                smap[c] = 1
        for c in t:
            if c in smap and smap[c] > 0:
                smap[c] -= 1
            else:
                return False
        for c in smap.keys():
            if smap[c] > 0:
                return False
        return True
