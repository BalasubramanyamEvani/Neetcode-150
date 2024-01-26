class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        tmp = pow(x, n // 2)
        if n % 2 == 0:
            return tmp * tmp
        return x * tmp * tmp
