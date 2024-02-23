class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        N2 = len(s2)
        N1 = len(s1)
        if N2 < N1:
            return False
        def matches(t1, t2):
            for k in t1.keys():
                if k not in t2 or t1[k] != t2[k]:
                    return False
            return True
        counts1 = {}
        counts2 = {}
        for i in range(ord('a'), ord('z') + 1):
            counts1[chr(i)] = 0
            counts2[chr(i)] = 0
        for ch1 in s1:
            counts1[ch1] = counts1.get(ch1, 0) + 1
        l = 0
        r = l + N1 - 1
        for j in range(l, r + 1):
            counts2[s2[j]] += 1
        while l < N2 - N1 + 1:
            if matches(counts1, counts2):
                return True
            if l < N2:
                counts2[s2[l]] -= 1
            if r + 1 < N2:
                counts2[s2[r + 1]] += 1
            l += 1
            r += 1
        return False
