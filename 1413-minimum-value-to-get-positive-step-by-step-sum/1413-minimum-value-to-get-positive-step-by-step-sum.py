class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ret = 1
        currsum = 1
        for num in nums:
            if currsum + num < 1:
                ret += 1 - (currsum + num)
                currsum = 1
            else:
                currsum += num
        return ret
