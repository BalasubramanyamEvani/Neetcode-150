class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        chs = []
        ptr = 0
        for i, ch in enumerate(s):
            if ptr < len(spaces) and i == spaces[ptr]:
                chs.append(" ")
                ptr += 1
            chs.append(ch)
        return "".join(chs)
