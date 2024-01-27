class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        offset = 0
        carry = 0
        N1 = len(num1)
        N2 = len(num2)
        res = [0 for _ in range(N1 + N2 + 1)]
        for i in range(N1 - 1, -1, -1):
            n1 = int(num1[i])
            ptr = 0
            for j in range(N2 - 1, -1, -1):
                n2 = int(num2[j])
                tmp = n1 * n2 + carry + res[ptr + offset]
                carry = tmp // 10
                res[ptr + offset] = tmp % 10
                ptr += 1
            if carry > 0:
                res[ptr + offset] = carry
                carry = 0
            offset += 1
        res = res[::-1]
        sindex = 0
        while sindex < len(res):
            if res[sindex] != 0:
                break
            sindex += 1
        res = res[sindex:]
        if not res:
            return "0"
        res = [str(c) for c in res]
        return "".join(res)
