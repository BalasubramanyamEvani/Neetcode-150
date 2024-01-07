import math

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        n = -x if x < 0 else x
        N = int(math.log10(n)) + 1
        res = 0
        for i in range(N - 1, -1, -1):
            rem = n % 10
            res += int(math.pow(10, i)) * rem
            n = n // 10
        if x < 0:
            res = -1 * res
        if res > math.pow(2, 31) - 1 or res < -math.pow(2, 31):
            return 0
        return res
