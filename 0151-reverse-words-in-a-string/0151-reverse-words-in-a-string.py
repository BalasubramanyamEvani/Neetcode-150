class Solution:
    def reverseWords(self, s: str) -> str:
        def getwords():
            ret = []
            curr = []
            for ch in s:
                if ch == " ":
                    ret.append("".join(curr))
                    curr = []
                else:
                    curr.append(ch)
            if curr:
                ret.append("".join(curr))
                curr = []
            return [word for word in ret if word]
        
        words = getwords()
        if not words:
            return []
        
        return " ".join(words[::-1])