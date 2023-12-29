class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        mem = {}
        for d in divisors:
            count = 0
            for num in nums:
                if num % d == 0:
                    count += 1
            mem[d] = count 
        res = sorted(mem.items(), key=lambda x: (-x[1], x[0]))
        return res[0][0]