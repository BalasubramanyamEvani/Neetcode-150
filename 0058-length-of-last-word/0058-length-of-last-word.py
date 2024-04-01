class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # last_word = s.strip().split()[-1]
        # res = len(last_word)
        # return res
        words = []
        currword = []
        for ch in s:
            if ch == " " and currword:
                words.append("".join(currword))
                currword = []
            elif ch != " ":
                currword.append(ch)
        if currword:
            words.append(currword)
        return len(words[-1])
