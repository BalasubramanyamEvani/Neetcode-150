class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1, n2 = len(word1), len(word2)
        if n1 != n2:
            return False
        c1 = Counter(word1)
        c2 = Counter(word2)
        k1, k2 = c1.keys(), c2.keys()
        if k1 != k2:
            return False
        v1, v2 = Counter(c1.values()), Counter(c2.values())
        return v1 == v2
