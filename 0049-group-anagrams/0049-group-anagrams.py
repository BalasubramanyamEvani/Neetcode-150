class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in mem:
                mem[key].append(s)
            else:
                mem[key] = [s]
        return [values for values in mem.values()]
