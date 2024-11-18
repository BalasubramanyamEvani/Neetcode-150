class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1, n2 = len(word1), len(word2)
        c1 = Counter(word1)
        c2 = Counter(word2)
        k1, k2 = c1.keys(), c2.keys()
        v1, v2 = Counter(c1.values()), Counter(c2.values())
        return n1 == n2 and k1 == k2 and v1 == v2
