class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_li = len(digits) - 1
        carry = 0
        res = []
        x = 0
        for i in range(digits_li, -1, -1):
            x = digits[i] + carry
            if i == digits_li:
                x += 1
            rem = x % 10
            carry = x // 10
            res.append(rem)
        if carry == 1:
            res.append(carry)
        return res[::-1]
