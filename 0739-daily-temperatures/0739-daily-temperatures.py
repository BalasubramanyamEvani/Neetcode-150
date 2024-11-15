class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        N = len(temperatures)
        ret = [0] * N
        for i in range(N):
            curr = temperatures[i]
            while stack and stack[-1][1] < curr:
                j, _ = stack.pop()
                ret[j] = i - j
            stack.append((i, curr))
        return ret
