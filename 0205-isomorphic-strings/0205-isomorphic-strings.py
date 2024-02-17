class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mem = {}
        revmem = {}
        N1 = len(s)
        N2 = len(t)
        if N1 != N2:
            return False
        for i in range(N1):
            ch1 = s[i]
            ch2 = t[i]
            if (ch1 in mem and mem[ch1] != ch2) or (ch2 in revmem and revmem[ch2] != ch1):
                return False
            mem[ch1] = ch2
            revmem[ch2] = ch1
        return True
