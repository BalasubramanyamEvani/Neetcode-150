class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        counts = {}
        for ch in t:
            counts[ch] = counts.get(ch, 0) + 1
        l = 0
        r = 0
        tmp = {}
        N = len(s)
        required = len(counts)
        retwin = math.inf
        retl, retr = -1, -1
        # construct a window
        while r < N:
            ch = s[r]
            tmp[ch] = tmp.get(ch, 0) + 1
            if ch in counts and counts[ch] == tmp[ch]:
                required -= 1
            # contract window to optimal
            while required == 0 and l <= r:
                winsize = r - l + 1
                if winsize < retwin:
                    retwin = winsize
                    retl, retr = l, r
                tmp[s[l]] -= 1
                if s[l] in counts and tmp[s[l]] < counts[s[l]]:
                    required += 1
                l += 1
            # move the window
            r += 1
        return s[retl:retr + 1] if retl != -1 else ""
