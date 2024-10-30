class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"])
        
        vowels_s = [ch for ch in s if ch in vowels][::-1]
        ret = []
        idx = 0
        for ch in s:
            if ch not in vowels:
                ret.append(ch)
            else:
                ret.append(vowels_s[idx])
                idx += 1
        return "".join(ret)
