class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Approach - 1
        # if n <= 0:
        #     return False
        # x = math.log2(n)
        # return int(x) == x
        
        # Approach - 2
        return n > 0 and (n & (~n + 1) == n)
