class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        mem = {
            0: -1
        }
        ret = 0
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in mem:
                ret = max(ret, i - mem[count])
            else:
                mem[count] = i
        return ret 
