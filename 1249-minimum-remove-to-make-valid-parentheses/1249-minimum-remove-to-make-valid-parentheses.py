class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()
        opened = 0
        for ch in s:
            if ch != "(" and ch != ")":
                stack.append(ch)
            elif ch == "(":
                opened += 1
                stack.append(ch)
            elif opened > 0:
                opened -= 1
                stack.append(ch)
        ret = []
        while stack:
            ch = stack.pop()
            if ch == "(" and opened > 0:
                opened -= 1
                continue
            ret.append(ch)
        return "".join(ret)[::-1]
