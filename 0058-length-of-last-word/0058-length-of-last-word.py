class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.strip().split()[-1]
        res = len(last_word)
        return res
