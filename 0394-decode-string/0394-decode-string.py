class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        num = 0
        tmp = []
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch.isalpha():
                tmp.append(ch)
            elif ch == "[":
                stack.append((num, tmp))
                num = 0
                tmp = []
            else:
                prevnum, prevtmp = stack.pop()
                tmp = tmp * prevnum
                tmp = [*prevtmp, *tmp]
        return "".join(tmp)
