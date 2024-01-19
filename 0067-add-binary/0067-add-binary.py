class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        a = a[::-1]
        b = b[::-1]
        N1 = len(a)
        N2 = len(b)
        N = max(N1, N2)
        ret = []
        for i in range(N):
            tmp = 0
            if i < N1:
                tmp += int(a[i])
            if i < N2:
                tmp += int(b[i])
            tmp += carry
            if tmp == 0:
                ret.append("0")
                carry = 0
            elif tmp == 1:
                ret.append("1")
                carry = 0
            elif tmp == 2:
                ret.append("0")
                carry = 1
            elif tmp == 3:
                ret.append("1")
                carry = 1
        if carry == 1:
            ret.append("1")
        return "".join(ret)[::-1]
