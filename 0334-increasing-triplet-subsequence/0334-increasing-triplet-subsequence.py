class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = []
        # modification of LIS, O(Nlog3) ~ O(N)
        # no extra space used
        for num in nums:
            index = bisect_left(dp, num)
            if index == len(dp):
                dp.append(num)
            else:
                dp[index] = num
            if len(dp) == 3:
                return True
        return False
