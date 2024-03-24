class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        currline = []
        currline_len = 0
        for word in words:
            if currline_len + len(word) + len(currline) > maxWidth:
                num_words = len(currline)

                total_spaces = maxWidth - currline_len
                spaces_between_words = total_spaces
                if num_words > 1:
                    remain_spaces = 0
                    spaces_between_words //= (num_words - 1)
                    remain_spaces = total_spaces % (num_words - 1)
                    for i, w in enumerate(currline):
                        if i < num_words - 1:
                            w += " " * spaces_between_words
                            if remain_spaces > 0:
                                w += " "
                                remain_spaces -= 1
                        currline[i] = w
                else:
                    currline[0] = currline[0] + " " * spaces_between_words
                ret.append("".join(currline))
                currline = []
                currline_len = 0
                
            currline.append(word)
            currline_len += len(word)
        
        if currline:
            spaces = maxWidth - (currline_len + len(currline) - 1)
            lastline = " ".join(currline) + " " * spaces
            ret.append(lastline)
        
        return ret
