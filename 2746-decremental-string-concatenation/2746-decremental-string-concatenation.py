class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        N = len(words)
        @cache
        def dfs(index, first_char, last_char):
            if index == N:
                return 0
            
            best = math.inf
            currword = words[index]
            cost = len(currword)
            
            # 1. join(stri - 1, words[i])
            c1 = dfs(index + 1, first_char, currword[-1])
            if last_char == currword[0]:
                best = min(best, c1 + cost - 1)
            else:
                best = min(best, c1 + cost)
            
            # 2. join(words[i], stri - 1)
            c2 = dfs(index + 1, currword[0], last_char)
            if first_char == currword[-1]:
                best = min(best, c2 + cost - 1)
            else:
                best = min(best, c2 + cost)
        
            return best
        
        return dfs(1, words[0][0], words[0][-1]) + len(words[0])
