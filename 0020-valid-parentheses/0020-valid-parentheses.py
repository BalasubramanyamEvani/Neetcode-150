class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mem = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        opened = mem.values()
        for ch in s:
            if ch in opened:
                stack.append(ch)
            elif stack and mem[ch] == stack[-1]:
                stack.pop()
            else:
                return False
        return True if not stack else False
        