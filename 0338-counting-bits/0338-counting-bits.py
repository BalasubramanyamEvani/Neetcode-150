class Solution:
    def countBits(self, n: int) -> List[int]:
        # divide and conquer
        def count_ones(n):
            mask1 = 0x55555555
            mask2 = 0x33333333
            mask3 = 0x0f0f0f0f
            mask4 = 0x00ff00ff
            mask5 = 0x0000ffff
            
            ret = n
            ret = (ret & mask1) + ((ret >> 1) & mask1)
            ret = (ret & mask2) + ((ret >> 2) & mask2)
            ret = (ret & mask3) + ((ret >> 4) & mask3)
            ret = (ret & mask4) + ((ret >> 8) & mask4)
            ret = (ret & mask5) + ((ret >> 16) & mask5)
            
            return ret
        
        ans = []
        for num in range(0, n + 1):
            ones = count_ones(num)
            ans.append(ones)
        
        return ans
