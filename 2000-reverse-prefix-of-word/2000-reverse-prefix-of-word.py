class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        if index == -1:
            return word
        chars = [ch for ch in word]
        l, r = 0, index
        while l < r:
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1
        return "".join(chars)
