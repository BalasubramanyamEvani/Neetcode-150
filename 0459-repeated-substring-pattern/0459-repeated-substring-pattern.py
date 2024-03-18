class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def factorize(n):
            factors = []
            l, r = 1, int(math.sqrt(n))
            for i in range(l, r + 1):
                if n % i == 0:
                    factors.append(i)
                    if i != 1:
                        factors.append(n // i)
            return factors
        
        N = len(s)
        if N == 1:
            return False
        factors = factorize(N)
        for factor in factors:
            multiple = N // factor
            substring = s[:factor]
            if substring * multiple == s:
                return True
        return False
    