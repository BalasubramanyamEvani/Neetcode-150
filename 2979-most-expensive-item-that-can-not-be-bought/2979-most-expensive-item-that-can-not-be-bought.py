class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        dp = [True] * 100001
        ret = -1
        tmp = min(primeOne, primeTwo)
        num = 1
        while num <= 100000:
            tmp1 = dp[num - primeOne] if num - primeOne >= 0 else False
            tmp2 = dp[num - primeTwo] if num - primeTwo >= 0 else False
            dp[num] = tmp1 or tmp2
            if not dp[num]:
                ret = num
            num += 1
        return ret
