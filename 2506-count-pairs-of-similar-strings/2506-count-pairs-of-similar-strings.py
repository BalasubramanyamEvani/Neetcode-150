class Solution:
    def similarPairs(self, words: List[str]) -> int:
        mem = {}
        for word in words:
            key = tuple(sorted(set(word)))
            mem[key] = mem.get(key, 0) + 1
        count = 0
        for v in mem.values():
            count += (v * (v - 1)) // 2
        return count
