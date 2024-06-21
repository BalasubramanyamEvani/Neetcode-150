class Solution:
    def minLength(self, s: str) -> int:
        stack = deque()
        for ch in s:
            if not stack:
                stack.append(ch)
            elif (stack[-1] + ch == "CD") or (stack[-1] + ch == "AB"):
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)
