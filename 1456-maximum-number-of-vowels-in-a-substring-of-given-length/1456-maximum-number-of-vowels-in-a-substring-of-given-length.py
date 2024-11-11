class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        l, r = 0, 0
        count = 0
        vowels = set(["a", "e", "i", "o", "u"])
        currmax = 0
        while r < n:
            count += 1 if s[r] in vowels else 0
            if r - l + 1 == k:
                currmax = max(currmax, count)
                count -= 1 if s[l] in vowels else 0
                l += 1
            r += 1
        return currmax
