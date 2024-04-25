class Solution:
    def myPow(self, x: float, n: int) -> float:
        def dfs(a, N):
            if N == 0:
                return 1
            if N == 1:
                return a
            if N < 0:
                num = 1.0 / dfs(a, -N // 2)
            else:
                num = dfs(a, N // 2)
            if N % 2 == 0:
                return num * num
            return num * num * (a if N > 0 else 1 / a)
        # log(N) complexity
        return dfs(x, n)
