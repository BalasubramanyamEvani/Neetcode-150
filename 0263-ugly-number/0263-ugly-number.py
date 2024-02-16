class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False
        mem = []
        def primes(n):
            if n % 2 == 0:
                mem.append(2)
            while n % 2 == 0:
                n = n // 2
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    mem.append(i)
                while n % i == 0:
                    n = n // i
            if n > 2:
                mem.append(n)
        primes(n)
        return mem[0] >= 2 and mem[-1] <= 5
