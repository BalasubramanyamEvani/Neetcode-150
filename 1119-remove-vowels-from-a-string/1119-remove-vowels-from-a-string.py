class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u"])
        ret = [ch for ch in s if ch not in vowels]
        return "".join(ret)
        