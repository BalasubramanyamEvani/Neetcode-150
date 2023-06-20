class Solution:
    def arraySign(self, nums: List[int]) -> int:
        numpos = 0
        numneg = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                numneg += 1
        if numneg % 2 == 0 or numneg == 0:
            return 1
        return -1
