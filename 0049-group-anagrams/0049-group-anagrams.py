class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = {}
        keys = set()
        for s in strs:
            key = "".join(sorted(s))
            if key in keys:
                mem[key].append(s)
            else:
                mem[key] = [s]
                keys.add(key)
        return [values for values in mem.values()]
