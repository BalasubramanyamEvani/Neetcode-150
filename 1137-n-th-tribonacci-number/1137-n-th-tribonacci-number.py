class Solution:
    def tribonacci(self, n: int) -> int:
        # mem = {}
        # def recur(num):
        #     if num <= 1:
        #         return num
        #     if num == 2:
        #         return 1
        #     if num in mem:
        #         return mem[num]
        #     mem[num] = recur(num - 1) + recur(num - 2) + recur(num - 3)
        #     return mem[num]
        # return recur(n)
        if n <= 1:
            return n
        if n == 2:
            return 1
        a = 0
        b = 1
        c = 1
        for _ in range(3, n + 1):
            tmp = a + b + c
            a = b
            b = c
            c = tmp
        return c
