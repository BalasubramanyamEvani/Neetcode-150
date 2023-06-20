class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        numslen = len(nums)
        if numslen == 1:
            return True
        mode = None
        for i in range(1, numslen):
            curr = None
            if nums[i] > nums[i - 1]:
                curr = True
            if nums[i] < nums[i - 1]:
                curr = False
            
            if curr is not None:
                if mode is None:
                    mode = curr
                elif mode != curr:
                    return False
        return True
            