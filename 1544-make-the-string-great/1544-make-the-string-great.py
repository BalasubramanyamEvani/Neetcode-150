class Solution:
    def makeGood(self, s: str) -> str:
        stack = deque()
        for ch in s:
            if stack:
                if stack[-1].lower() == ch.lower() and ord(stack[-1]) != ord(ch):
                    stack.pop()
                    continue
            stack.append(ch)
        return "".join(list(stack))
