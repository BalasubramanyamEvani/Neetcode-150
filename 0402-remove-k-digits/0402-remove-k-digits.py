class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque()
        # maintain monotonic increasing stack and
        # elimate number according to k
        for n in num:
            while stack and k > 0 and int(stack[-1]) > int(n):
                stack.pop()
                k -= 1
            stack.append(n)
        while k > 0 and stack:
            stack.pop()
            k -= 1
        if not stack:
            return "0"
        ret = "".join(stack)
        i = 0
        N = len(ret)
        while i < N:
            if ret[i] != "0":
                break
            i += 1
        return ret[i:] if i < N else "0"
