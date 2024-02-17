class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def recursive(opened, closed, tmp):
            if len(tmp) == 2*n:
                ret.append("".join(tmp))
            if opened < n:
                tmp.append("(")
                recursive(opened + 1, closed, tmp)
                tmp.pop()
            if closed < n and closed < opened:
                tmp.append(")")
                recursive(opened, closed + 1, tmp)
                tmp.pop()
        recursive(0, 0, [])
        return ret