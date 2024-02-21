class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ret = []
        for s in strs:
            slen = str(len(s))
            ret.append(slen + "#" + s)
        return "".join(ret)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        N = len(s)
        ret = []
        while i < N:
            j = i
            while s[j] != "#" and j < N:
                j += 1
            slen = int(s[i:j])
            ret.append(s[j + 1:j + 1 + slen])
            i = j + 1 + slen
        return ret

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))