class Solution:
    def hammingWeight(self, n: int) -> int:
        one_bit_mask = 0x55555555
        two_bit_mask = 0x33333333
        four_bit_mask = 0x0f0f0f0f
        eight_bit_mask = 0x00ff00ff
        sixteen_bit_mask = 0x0000ffff
        res = (n & one_bit_mask) + ((n >> 1) & one_bit_mask)
        res = (res & two_bit_mask) + ((res >> 2) & two_bit_mask)
        res = (res & four_bit_mask) + ((res >> 4) & four_bit_mask)
        res = (res & eight_bit_mask) + ((res >> 8) & eight_bit_mask)
        res = (res & sixteen_bit_mask) + ((res >> 16) & sixteen_bit_mask)
        return res
