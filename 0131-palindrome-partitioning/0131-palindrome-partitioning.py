class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(tmp):
            l, r = 0, len(tmp) - 1
            while l < r:
                if tmp[l] != tmp[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        N = len(s)
        ret = []
        def dfs(tmp, index):
            if index >= N:
                ret.append(tmp[:])
            n = N - index
            for i in range(n):
                partition = s[index: index + i + 1]
                if isPalindrome(partition):
                    tmp.append(partition)
                    dfs(tmp, index + i + 1)
                    tmp.pop()

        dfs([], 0)
        return ret
