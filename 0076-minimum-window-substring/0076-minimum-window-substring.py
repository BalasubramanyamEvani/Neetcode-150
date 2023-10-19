class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mem = {}
        tmp = {}
        for c in t:
            if c in mem:
                mem[c] += 1
            else:
                mem[c] = 1
                tmp[c] = 0
        l = 0
        r = 0
        min_l, min_r = -1, -1
        res = len(s) + 1
        
        def update_pos(rpos, lpos):
            nonlocal res, min_l, min_r
            if rpos - lpos < res:
                min_l = lpos
                min_r = rpos - 1
                res = rpos - lpos
        
        mem_key_cntr = len(mem)
        
        while r < len(s):
            if s[r] in mem:
                tmp[s[r]] += 1
                if tmp[s[r]] == mem[s[r]]:
                    mem_key_cntr -= 1
            r += 1
            if mem_key_cntr == 0:
                while l < r:
                    update_pos(r, l)
                    if s[l] in mem:
                        tmp[s[l]] -= 1
                        if tmp[s[l]] < mem[s[l]]:
                            mem_key_cntr += 1
                            l += 1
                            break
                    l += 1
        
        if min_l != -1:
            return s[min_l: min_r + 1]
        
        return ""
