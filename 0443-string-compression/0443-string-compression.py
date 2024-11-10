class Solution:
    def compress(self, chars: List[str]) -> int:
        def add(ptr, ch, num):
            s = ch + (str(num) if num > 1 else "")
            for ch in s:
                chars[ptr] = ch
                ptr += 1
            return ptr
        
        ptr = 0
        count = 1
        prev = chars[0]
        N = len(chars)
        for i in range(1, N):
            ch = chars[i]
            if ch == prev:
                count += 1
            else:
                ptr = add(ptr, prev, count)
                count = 1
                prev = ch
        
        ptr = add(ptr, prev, count)
        return ptr
