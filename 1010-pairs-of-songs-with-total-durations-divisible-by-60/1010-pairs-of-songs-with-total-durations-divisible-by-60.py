class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mem = {}
        for i in range(60):
            mem[i] = 0
        ans = 0
        for t in time:
            rem = t % 60
            if rem == 0:
                ans += mem[rem]
            else:
                ans += mem[60 - rem]
            mem[rem] += 1
        return ans
