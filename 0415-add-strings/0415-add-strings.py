class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        l = max(l1, l2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = []
        carry = 0
        for i in range(0, l, 1):
            s = 0
            if i < l1:
                s += int(num1[i])
            if i < l2:
                s += int(num2[i])
            cs = s + carry
            carry = cs // 10
            rem = cs % 10
            res.append(str(rem))
        if carry != 0:
            res.append(str(carry))
        return "".join(res[::-1])
