class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1Parts = [int(num) for num in version1.split(".")]
        v2Parts = [int(num) for num in version2.split(".")]
        N1, N2 = len(v1Parts), len(v2Parts)
        maxnum = max(N1, N2)
        v1Parts = v1Parts + [0] * (maxnum - N1)
        v2Parts = v2Parts + [0] * (maxnum - N2)
        i, j = 0, 0
        print(v1Parts, v2Parts)
        while i < maxnum:
            if v1Parts[i] > v2Parts[i]:
                return 1
            if v1Parts[i] < v2Parts[i]:
                return -1
            i += 1
        return 0
        