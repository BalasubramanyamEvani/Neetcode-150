class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countOnes(num):
            mask1 = 0x55555555
            mask2 = 0x33333333
            mask3 = 0x0f0f0f0f
            mask4 = 0x00ff00ff
            mask5 = 0x0000ffff
            num = (num & mask1) + ((num >> 1) & mask1)
            num = (num & mask2) + ((num >> 2) & mask2)
            num = (num & mask3) + ((num >> 4) & mask3)
            num = (num & mask4) + ((num >> 8) & mask4)
            num = (num & mask5) + ((num >> 16) & mask5)
            return num
        
        ret = sorted(arr, key=lambda x: (countOnes(x), x))
        return ret
