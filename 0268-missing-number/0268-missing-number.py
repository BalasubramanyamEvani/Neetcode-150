class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Math solution
        
        # n = len(nums)
        # sumx = 0
        # for num in nums:
        #     sumx += num
        # shouldbe = n * (n + 1)//2
        # return shouldbe - sumx
        
        # bitwise solution
        n = len(nums)
        ret = n
        for i in range(0, n):
            ret ^= i ^ nums[i]
        return ret
    