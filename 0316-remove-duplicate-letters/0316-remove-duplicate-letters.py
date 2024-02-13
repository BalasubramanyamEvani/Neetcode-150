class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        N = len(s)
        seen = set()
        occs = {}
        for i, ch in enumerate(s):
            occs[ch] = i
        stack = deque()
        for i, ch in enumerate(s):
            if ch not in seen:
                while stack and ch < stack[-1] and i < occs[stack[-1]]:
                    top = stack.pop()
                    seen.remove(top)
                stack.append(ch)
                seen.add(ch)
        ret = []
        while stack:
            ret.append(stack.pop())
        return "".join(ret)[::-1]
