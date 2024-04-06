class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        N = len(nums)
        count = 0
        
        def gcd(a, b):
            if a == 0:
                return b
            if b == 0:
                return a
            if a == b:
                return a
            return gcd(b % a, a) 
        
        for i in range(N - 1):
            first = int(str(nums[i])[0])
            for j in range(i + 1, N):
                last = int(str(nums[j])[-1])
                if gcd(first, last) == 1:
                    count += 1
        return count
                