class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def create_count_map(s):
            res = {}
            for c in s:
                if c in res:
                    res[c] += 1
                else:
                    res[c] = 0
            return res
        
        def is_possible(md, ms):
            for key in md.keys():
                if key not in ms or md[key] > ms[key]:
                    return False
            return True
        
        chars_count_map = create_count_map(chars)
        res = 0
        for word in words:
            word_count_map = create_count_map(word)
            if is_possible(word_count_map, chars_count_map):
                res += len(word)
        
        return res
        