class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        i = 0
        j = 1
        currmin = prices[0]
        ret = 0
        while j < N:
            if prices[j] < currmin:
                currmin = prices[j]
            else:
                ret = max(prices[j] - currmin, ret)
            j += 1
        return ret
        