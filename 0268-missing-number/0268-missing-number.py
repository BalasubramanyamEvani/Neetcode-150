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
        N = len(nums)
        ret = N
        for i in range(0, N):
            ret = ret ^ (i ^ nums[i])
        return ret
