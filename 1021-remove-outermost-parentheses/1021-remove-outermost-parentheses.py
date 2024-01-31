class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        ret = []
        for ch in s:
            if ch == "(":
                count += 1
                if count - 1 == 0:
                    continue
            if ch == ")":
                count -= 1
            if count > 0:
                ret.append(ch)
        return "".join(ret)
