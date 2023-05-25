class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []
        for c in s:
            ch = c
            if ord(c) >= 65 and ord(c) <= 90:
                ch = chr(ord(c) + 32)
            res.append(ch)
        res = "".join(res)
        return res
