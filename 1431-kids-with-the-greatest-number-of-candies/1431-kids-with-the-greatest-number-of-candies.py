class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_amt = max(candies)
        return [amt + extraCandies >= max_amt for amt in candies]
