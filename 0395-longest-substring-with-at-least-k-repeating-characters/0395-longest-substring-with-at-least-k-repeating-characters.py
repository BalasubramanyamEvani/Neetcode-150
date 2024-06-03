class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ret = 0
        for uniques in range(1, 27):
            left = 0
            count = Counter()
            for right, ch in enumerate(s):
                count[ch] += 1
                while len(count) > uniques:
                    count[s[left]] -= 1
                    if count[s[left]] == 0:
                        del count[s[left]]
                    left += 1
                all_atleast_k = True
                for _, v in count.items():
                    if v < k:
                        all_atleast_k = False
                if all_atleast_k:
                    ret = max(ret, right - left + 1)
        return ret
