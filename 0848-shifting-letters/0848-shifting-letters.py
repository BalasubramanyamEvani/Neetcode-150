class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        N = len(s)
        final_shifts = [0 for _ in range(N)]
        for i in range(N):
            final_shifts[0] += shifts[i]
            if i + 1 < N:
                final_shifts[i + 1] -= shifts[i]
        ret = []
        psum = 0
        for i, ch in enumerate(s):
            psum += final_shifts[i]
            shift = (ord(ch) - ord('a') + psum) % 26
            shifted_chr = chr(ord('a') + shift)
            ret.append(shifted_chr)
        return "".join(ret)
