class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        joined_str = []
        word1_start, word1_end = 0, len(word1)  - 1
        word2_start, word2_end = 0, len(word2) - 1
        while word1_start <= word1_end and word2_start <= word2_end:
            joined_str.append(word1[word1_start])
            joined_str.append(word2[word2_start])
            
            word1_start += 1
            word2_start += 1
        
        while word1_start <= word1_end:
            joined_str.append(word1[word1_start])
            word1_start += 1
        
        while word2_start <= word2_end:
            joined_str.append(word2[word2_start])
            word2_start += 1
        
        joined_str = "".join(joined_str)
        return joined_str
            