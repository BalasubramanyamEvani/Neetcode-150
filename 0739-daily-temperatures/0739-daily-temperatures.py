class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        N = len(temperatures)
        ret = [0 for _ in range(N)]
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                j, _ = stack.pop()
                ret[j] = i - j
            stack.append((i, temp))
        return ret
