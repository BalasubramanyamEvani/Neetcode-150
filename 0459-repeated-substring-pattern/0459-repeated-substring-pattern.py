class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def factorize(x):
            if x == 1:
                return []
            res1 = []
            res2 = []
            lim = int(math.sqrt(x))
            for i in range(1, lim + 1):
                if x % i == 0:
                    res1.append(i)
                    if i != 1:
                        res2.append(x // i)
            return res1 + res2[::-1]
        
        slen = len(s)
        factors = factorize(slen)
        for factor in factors:
            times = slen // factor
            if s[0: factor] * times == s:
                return True
        return False
        