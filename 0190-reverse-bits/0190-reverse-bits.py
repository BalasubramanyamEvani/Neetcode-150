class Solution:
    def reverseBits(self, n: int) -> int:
        ret = n
        
        # divide and conquer
        mask1 = 0x55555555
        mask2 = 0x33333333
        mask3 = 0x0f0f0f0f
        mask4 = 0x00ff00ff
        mask5 = 0x0000ffff

        ret = ((ret & mask1) << 1) | ((ret >> 1) & mask1)
        ret = ((ret & mask2) << 2) | ((ret >> 2) & mask2)
        ret = ((ret & mask3) << 4) | ((ret >> 4) & mask3)
        ret = ((ret & mask4) << 8) | ((ret >> 8) & mask4)
        ret = ((ret & mask5) << 16) | ((ret >> 16) & mask5)
        
        return ret
